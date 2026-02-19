


def nombre():
    print('Hola mundo')
nombre()

def suma():
    a=6
    print("Dentro de la funcion: ",a)
    b=7
    c=a+b
    return c


a=3
print("la suma es: ",suma())
print("fuera de la funcion; ",a)
b=7
c=a+b

def multiplica(a,b):
    return a*b
print("la multiplicacion es: ",multiplica(6,7))