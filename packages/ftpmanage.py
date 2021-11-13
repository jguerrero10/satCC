# -*- coding: utf-8 -*-

""" 
Created on 2016-02-24 18:13:05

@author: Joel Guerrero - Canal Clima

Envio de datos a traves de FTP
"""

from ftplib import FTP
from pathlib import PurePath
from packages.log import log_create

def ftpsend(server, user, clave, folder, file, dirfile):
    file_origin = PurePath(dirfile, file)
    try: 
        f = open(file_origin, 'rb')   
        try:
            ftp = FTP(server, encoding='Latin-1')
            ftp.login(user, clave)
            ftp.cwd(folder)
            ftp.storbinary(f'STOR {file}', f)
            log_create(f"Archivo {file} enviado correctamente", 'info')
            f.close()
            ftp.quit()        
        except ValueError as err:
            log_create(f"Error de conexion al servidor: {err}")            
    except ValueError as err:
        log_create(f"Error al leer el archivo Local {err}")        
    return

