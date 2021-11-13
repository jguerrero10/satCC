# -*- coding: utf-8 -*-

""" 
Created on 2021-11-12 19:51:00

@author: Joel Guerrero - Canal Clima

Programa principal, donde permite la conexion serial a traves
de un socket TCP/IP

*** La configuracion esta en el paquete Setting
*** La plantilla base se encuentra en Template
*** Los Paquetes para FTP, Creacion de archivos, 
    generacion de logs se encuentran en packages
*** Los logs se encuentran en log
"""

import serial
import jinja2
from packages.filemanage import *
from packages.ftpmanage import *
from packages.log import *
from settings import config
from datetime import datetime

def main_sat():   

    def render_template(datos_list):
        nombre = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')    
        file = creartxt(f'{nombre}{NAME_STATION}.dat', DIR_DATOS)
        log_create(f"Se crea el archivo {file}", 'info')    
        datos = template.render(datos = datos_list, estacion=NAME_STATION)
        try:
            grabartxt(DIR_DATOS, file, datos)
        except:
            log_create(f"Error al grabar datos en {file}", 'warning')        
        ftpsend(ftp['SERVER'], ftp['USER'], ftp['PASS'], ftp['DIR'], file, DIR_DATOS)
        return
      
    datos = list()
    conteo = 0
    while True:
        try:
            with serial.serial_for_url(socket_serial, baudrate, timeout=1) as ser:       
                ser.reset_input_buffer()
                x = ser.read(100)                   
                if x != b'':
                    linea = x.decode('utf-8')
                    datos.append(linea)
                    conteo += 1
                if conteo > 4:
                    conteo = 0            
                    render_template(datos)
                    datos.clear()
        except serial.SerialException as e:
            log_create(e)
            pass
        except OSError as e:
            log_create(e)

if __name__ == "__main__":
    log_create('Programa Iniciado...........', 'info')
    loaderTemp = jinja2.FileSystemLoader(searchpath="./template/")
    envTemp = jinja2.Environment(loader=loaderTemp)
    template_file = 'template.html'
    template = envTemp.get_template(template_file)
    
    DIR_DATOS = config.DIR_DATOS
    NAME_STATION = config.NAME_STATION
    ip = config.IP_DEVICE
    puerto = config.PORT_TCP

    socket_serial = f'socket://{ip}:{puerto}'
    log_create(f'Socket {socket_serial}', 'info')    
    baudrate = config.BAUDRATE_SERIAL

    ftp = config.FTP_CREDENTIALS    
    main_sat()    
else:
    log_create('main.py no debe ser importado, por favor ejecutalo como principal', 'warning')    