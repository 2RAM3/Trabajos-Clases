"""
Nombre: Circunferencia.py
Objetivo: Es la subclase de punto 
Autor: Tomas Ramirez
Fecha: 9/11/2019
"""
from Punto import Punto

class Circunferencia(Punto):
    #Metodo constructor
    def __init__(self,valorX,valorY,vradio):
        #actualizar el atributo
        self.radio=vradio
        #Actualizar los atributos de Punto
        Punto.__init__(self,valorX,valorY)

    #Lista de metodos get
    def getRadio(self):
        return self.radio
    #lista de metodos set 
    def setRadio(self,vradio):
        self.radio=vradio
    def toString(self):
        return "El radio es: ",str(self.radio)