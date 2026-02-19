import os
def suma():
    os.system("cls")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    return a+b
def resta():
    os.system("cls")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    return a-b
def multiplicar():
    os.system("cls")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    return a*b
def dividir():
    os.system("cls")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    if b==0:
        return "Error division entre 0"
    return a/b

def menu():
    while True:
        os.system("cls")
        print("Menu de operciones \n1.- +\n2.- -\n3.- *\n4.- /\n5.- Salir")
        opmenu=int(input("Elige una opcion: "))
        if opmenu>5:
            print("Opcion no valida")
            input("")
        if opmenu==5:
            break
        if opmenu==1:
            print("El resultado es; ",suma())
            input("")
        if opmenu==2:
            print("El resultado es; ",resta())
            input("")
        if opmenu==3:
            print("El resultado es; ",multiplicar())
            input("")
        if opmenu==4:
            print("El resultado es; ",dividir())
            input("")
menu()



    
   