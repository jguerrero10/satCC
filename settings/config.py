from pathlib import PurePath
import environ

env = environ.Env(
        DEBUG=(bool, False)
)

#Leyendo archivo .env
environ.Env.read_env()

# Datos Estaciones
NAME_STATION = env('NAME_STATION') # Nombre Estacion
IP_DEVICE = env('IP_DEVICE') # IP Estacion
PORT_TCP = env('PORT_TCP') # Puerto Estacion
BAUDRATE_SERIAL = env.int('BAUDRATE_SERIAL')

# Directorio de datos
DIR_DATOS = PurePath('.', 'datos')

# FTP
FTP_CREDENTIALS = {
        'SERVER': env('SERVER'),
        'USER': env('USER'),
        'PASS': env('PASS'),
        'DIR': env('DIR')
}