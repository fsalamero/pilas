# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

VELOCIDAD = 4


class Martian(Actor):

    def __init__(self, x=0, y=0):
        Actor.__init__(self, x=x, y=y)
        self.animacion = pilas.imagenes.Grilla("marcianitos/martian.png", 12)
        self.definir_cuadro(0)
        self.hacer(Esperando())

    def definir_cuadro(self, indice):
        self.animacion.definir_cuadro(indice)
        self.animacion.asignar(self)

class Esperando(Comportamiento):
    "Un actor en posicion normal o esperando a que el usuario pulse alguna tecla."

    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(0)

    def actualizar(self):
        if pilas.mundo.control.izquierda:
            self.receptor.espejado = True
            self.receptor.hacer(Caminando())
        elif pilas.mundo.control.derecha:
            self.receptor.espejado = False
            self.receptor.hacer(Caminando())

        if pilas.mundo.control.arriba:
            self.receptor.hacer(Saltando())


class Caminando(Comportamiento):

    def __init__(self):
        self.cuadros = [1, 1, 1, 2, 2, 2]
        self.paso = 0

    def actualizar(self):
        self.avanzar_animacion()

        if pilas.mundo.control.izquierda:
            self.receptor.x -= VELOCIDAD
        elif pilas.mundo.control.derecha:
            self.receptor.x += VELOCIDAD
        else:
            self.receptor.hacer(Esperando())

        if pilas.mundo.control.arriba:
            self.receptor.hacer(Saltando())


    def avanzar_animacion(self):
        self.paso += 1

        if self.paso >= len(self.cuadros):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.paso])

class Saltando(Comportamiento):

    def __init__(self):
        self.dy = 8
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(3)

    def actualizar(self):
        self.receptor.y += self.dy
        self.dy -= 0.3

        if self.receptor.y < 0:
            self.receptor.y = 0
            self.receptor.hacer(Esperando())

        if pilas.mundo.control.izquierda:
            self.receptor.espejado = True
            self.receptor.x -= VELOCIDAD
        elif pilas.mundo.control.derecha:
            self.receptor.espejado = False
            self.receptor.x += VELOCIDAD
