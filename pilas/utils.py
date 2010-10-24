# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import os
import shutil
import interpolaciones
import sys
import subprocess
import math

import pilas
from PySFML import sf


PATH = os.path.dirname(os.path.abspath(__file__))


def cargar_autocompletado():
    "Carga los modulos de python para autocompletar desde la consola interactiva."
    import rlcompleter
    import readline

    readline.parse_and_bind("tab: complete")

def hacer_flotante_la_ventana():
    "Hace flotante la ventana para i3 (el manejador de ventanas que utiliza hugo...)"
    try:
        subprocess.call(['i3-msg', 't'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError:
        pass

def es_interpolacion(an_object):
    "Indica si un objeto se comporta como una colisión."

    return isinstance(an_object, interpolaciones.Interpolacion)


def obtener_ruta_al_recurso(ruta):
    """Busca la ruta a un archivo de recursos.

    Los archivos de recursos (como las imagenes) se buscan en varios
    directorios (ver docstring de image.load), así que esta
    función intentará dar con el archivo en cuestión.
    """

    dirs = ['./', os.path.dirname(sys.argv[0]), 'data', PATH, PATH + '/data']


    for x in dirs:
        full_path = os.path.join(x, ruta)
        #DEBUG: print "buscando en: '%s'" %(full_path)

        if os.path.exists(full_path):
            return full_path

    # Si no ha encontrado el archivo lo reporta.
    raise IOError("El archivo '%s' no existe." %(ruta))


def esta_en_sesion_interactiva():
    "Indica si pilas se ha ejecutado desde una consola interactiva de python."
    try:
        cursor = sys.ps1
        return True
    except AttributeError:
        return False

def distancia(a, b):
    "Retorna la distancia entre dos numeros."
    return abs(b - a)

def distancia_entre_dos_puntos((x1, y1), (x2, y2)):
    "Retorna la distancia entre dos puntos en dos dimensiones."
    return math.sqrt(distancia(x1, x2) ** 2 + distancia(y1, y2) ** 2)

def distancia_entre_dos_actores(a, b):
    return distancia_entre_dos_puntos((a.x, a.y), (b.x, b.y))

def colisionan(a, b):
    "Retorna True si dos actores estan en contacto."
    return distancia_entre_dos_actores(a, b) < a.radio_de_colision + b.radio_de_colision
    

def crear_juego():
    nombre = raw_input("Indica el nombre del juego: ")
    shutil.copytree(PATH + "/data/juegobase", nombre)

    print "Se ha creado el directorio '%s'" %(nombre)
    print "Ingresa en el directorio y econtrarás los archivos iniciales del juego."
