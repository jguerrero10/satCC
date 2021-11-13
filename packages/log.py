# -*- coding: utf-8 -*-

""" 
Created on 2021-11-11 13:05:00

@author: Joel Guerrero - Canal Clima

Generacion de Logs
"""

import logging
from datetime import datetime

logging.basicConfig(filename='./log/logs.log', encoding='utf-8', level=logging.INFO)
logging.basicConfig(filename='./log/logs.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='./log/logs.log', encoding='utf-8', level=logging.WARNING)
logging.basicConfig(filename='./log/logs.log', encoding='utf-8', level=logging.ERROR)
logging.basicConfig(filename='./log/logs.log', encoding='utf-8', level=logging.CRITICAL)


def log_create(e, tipo='error'):
    tiempo = datetime.now()
    if tipo == 'debug':
        logging.debug(f'{tiempo} -- {e}')
    elif tipo == 'info':
        logging.info(f'{tiempo} -- {e}')
    elif tipo == 'warning':
        logging.warning(f'{tiempo} -- {e}')
    else:
        logging.error(f'{tiempo} -- {e}')