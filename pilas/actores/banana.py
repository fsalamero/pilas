# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Actor

class Banana(Actor):
    "Representa una explosion para una bomba, dinamita etc..."

    def __init__(self, x=0, y=0):
        self.animacion = pilas.imagenes.cargar_grilla("banana.png", 2)
        Actor.__init__(self, x=x, y=y)
        self.definir_cuadro(0)

    def definir_cuadro(self, indice):
        self.animacion.definir_cuadro(indice)
        self.animacion.asignar(self)

    def abrir(self):
        self.definir_cuadro(1)

    def cerrar(self):
        self.definir_cuadro(0)
