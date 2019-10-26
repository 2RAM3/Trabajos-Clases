"""
Nombre: SolucionEjercicio.py
Objetivo: Resolver ejercicio 1
Autor: Tomas Ramirez
Fecha: 26 octubre de 2019
"""
def main():
    a = int(input("Ingresa sueldo:"))
    if int(a)< 1000:
        t=((a*.12)+a)     
        print(str(t) + " Triste")
              
    if int(a)>1000:
        t=((a*.15)+a)
        print(str(t) + " Sueldo")
        
if __name__ == "__main__":
    main()