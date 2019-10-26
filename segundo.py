"""
Nombre: SolucionEjercicio.py
Objetivo: Resolver ejercicio 1
Autor: Tomas Ramirez
Fecha: 26 octubre de 2019
"""
def main():
    while True :
        c=int(input("1.-Categoria 1 2.-Categoria 2  3.-Categoria 3  4.- Categoria 4: 5.-Salir: "))
        if (c==1):
            a = int(input("Ingresa sueldo:"))
            t=((a*.15)+a)     
            print(str(t) + " Aumento 15%")

        if (c==2):
            a = int(input("Ingresa sueldo:"))
            t=((a*.10)+a)     
            print(str(t) + " Aumento 10%")

        if (c==3):
            a = int(input("Ingresa sueldo:"))
            t=((a*.8)+a)     
            print(str(t) + " Aumento 8%")
        
        if (c==4):
            a = int(input("Ingresa sueldo:"))
            t=((a*.7)+a)     
            print(str(t) + " Aumento 7%")

        if (c==5):
            exit()
        
if __name__ == "__main__":
    main()