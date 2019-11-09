"""
Nombre: Cilindro.py
Objetivo: Es la subclase de circunferencia
Autor: Tomas Ramirez
Fecha: 9/11/2019
"""
from Circunferencia import Circunferencia
from Punto import Punto
class Cilindro(Circunferencia):
    #Metodo constructor
    def __init__(self,valorX,valorY,vradio,valtura):
        #Acturalizamos atributos del cilindro
        self.altura=valtura
        #Actualizamos las 
        Circunferencia.__init__(self,vradio)
        Punto.__init__(self,valorX,valorY)

    #Metodo get altura
    def getAltura(self):
        return self.altura
    #Metodo set altura
    def setAltura(self,valtura):
        self.altura=valtura
    #Metodos to String
    def toString(self):
        return "La altura del cilindro es: ",str(self.altura)

