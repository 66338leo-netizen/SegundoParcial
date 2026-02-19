
import os

op=1
num1=0
num2=0
num3=0

def cuadrado():
    Area=0
    print("Area de un Cuadrado: \n""")
    num1=int(input("Ingrese el valor de la base: "))
    num2=int(input("Ingrese el valor de la altura: "))
    Area=num1*num2
    print("El Area de la figura es: ",Area)
    input("")
def rectangulo():
    Area=0
    print("Area de un Rectangulo: \n""")
    num1=int(input("Ingrese el valor de la base: "))
    num2=int(input("Ingrese el valor de la altura: "))
    Area=num1*num2
    print("El Area de la figura es: ",Area)
    input("")

def triangulo():
    Area=0
    print("Area de un Triangulo: \n""")
    num1=int(input("Ingrese el valor de la base: "))
    num2=int(input("Ingrese el valor de la altura: "))
    Area=(num1*num2)/2
    print("El Area de la figura es: ",Area)
    input("")

def circulo():
    Area=0
    pi=3.1416
    print("Area de un Circulo: \n""")
    num1=int(input("Ingrese el valor del Radio: "))
    Area=pi(num1*num1)
    print("El Area de la figura es: ",Area)
    input("")

def trapecio():
    Area=0
    print("Area de un Trapecio: \n""")
    num1=int(input("Ingrese el valor de la Base mayor : "))
    num2=int(input("Ingrese el valor de la Base menor: "))
    num3=int(input("Ingrese el valor de la altura: "))
    Area=((num1+num2)*num3)/2
    print("El Area de la figura es: ",Area)
    input("")







def menu():
    while True:
        os.system("cls")
        print("Menu de Areas \n""\n1.- Cuadrado \n2.- Rectangulo \n3.- Triangulo \n4.- Circulo \n5.- Trapecio \n6.- Salir")
        op=int(input("Elige una opcion: "))
        if op==1:
            print(cuadrado())
        if op==2:
            print(rectangulo())
        if op==3:
            print(triangulo())
        if op==4:
            print(circulo())
        if op==5:
            print(trapecio())
        if op==0:
            break

    
    
if __name__==("__main__"):
    menu()

