# -*- coding: utf-8 -*-

""" 
Created on 2016-02-15 18:13:05

@author: Joel Guerrero - Yesid Amaya - Canal Clima

Este codigo permite generar y agregar datos en un archivos
"""

import os
import codecs

# Crear Archivo txt
def creartxt(namefile,dirfile):
    if not os.path.exists(dirfile): os.makedirs(dirfile)
    filename=os.path.join(dirfile,namefile)
    with open(filename,'a') as outfile:
        outfile.close()
    return namefile

# Grabar en archivo txt
def grabartxt(dirname,filename,data):
    namefilew=os.path.join(dirname,filename)
    with open(namefilew,'w') as archi:
        archi.write(data)
    return