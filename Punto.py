"""
Nombre: Punto.py
Objetivo: Es la super clases en la jerarquia de herencia
Autor: Tomas Ramirez
Fecha: 9/11/2019
"""

clase Punto(object):
    #Metodo constructor
    def__init__(self,valorX,valorY):
        #Creamos los actributos
        self.x=valorX
        self.y=valorY

    #Lista de metodos
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    #Lista de metodos set
    def setX(self,valorX):
        self.x=valorX
    def setY(self,valorY):
        self.y=valorY
    #Metodos  toString()
    def toString(self):
        return "Las coordenadas del punto son: ",str(self.x),",",str(self.y)

    