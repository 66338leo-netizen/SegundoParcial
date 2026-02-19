import os

def suma():
    os.system("cls")
    a=int(input("Numero1: "))
    b=int(input("Numero2: "))
    res=a+b
    print("La suma es: ",res)
    input()


def resta():
    os.system("cls")
    a=int(input("Numero1: "))
    b=int(input("Numero2: "))
    res=a+b
    print("La suma es: ",res)
    input()

def menu():
    op=0
    while op!=5:
        os.system("cls")
        print("Menu de operciones \n1.- +\n2.- -\n3.- *\n4.- /\n5.- Salir")
        op=int(input("Opcion; "))
        if op==1:
            suma()
        if op==2:
            resta()
            
