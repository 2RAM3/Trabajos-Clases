"""
Nombre: Cilindro.py
Objetivo: instanciar la clase cilindro
Autor: Tomas Ramirez
Fecha: 9/11/2019
"""
from tkinter import *
from Cilindro import Cilindro

def clicked():
    w=Tk()
    w.title("Resultado")
    w.geometry("400x300")

    lbl1=Label(w,text="La circunferencia: ")
    lbl1.grid(column=5,row=5)

def main():
    #Creamos ventana raiz
    w=Tk()
    #Atributos
    
    w.title("Objetos tipo Cilindro")
    w.geometry("400x300")

    lbl1=Label(w,text="Cordenada en X: ")
    lbl1.grid(column=5,row=5)
    txt = Entry(w,width=10)
    txt.grid(column=6, row=5)
    lbl2=Label(w,text="Cordenada en Y: ")
    lbl2.grid(column=5,row=8)
    txt2 =Entry(w,width=11)
    txt2.grid(column=6, row=8)
    btn = Button(w, text="Enviar",bg="blue", fg="black", command=clicked)
    btn.grid(column=6, row=10)   

    #Creamos  un objeto de la clase cilindro 
    #cil=Cilindro(10,10,12.13,25.11)

    #Hace un ciclo loop para que la ventana quede visible
    w.mainloop()

if __name__ == "__main__":
    main()



