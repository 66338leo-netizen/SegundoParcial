import os
ico=[]
alumno={
    "nombre":"",
    "edad": 0,
    "materia": "",
    "Calificacion": 0
}
i=0
suma=0
promedio=0
cont=1
os.system("cls")
cantidad=int(input("Cuantos alumnos se ingresaran: "))
print("")
for i in range(0,cantidad):
    print("--------Alumno {}---------".format(cont))
    a=input("Ingrese el nombre: ")
    b=int(input("Ingrese la edad: "))
    c=input("Ingrese la materia: ")
    d=float(input("Ingrese la calificacion: "))
    cont=cont+1
    
    alumno["nombre"] = a
    alumno["edad"] = b
    alumno["materia"] = c
    alumno["Calificacion"] = d
    ico.append(alumno.copy())
print("Lista de alumnos ingresados: ")
print("")
print("La cantidad de alumnos ingresados es: ",cantidad)


for alumno in ico:
    suma+=alumno["Calificacion"]
    print(alumno)
    print("")
promedio= suma/len(ico)
print("El promedio de los alumnos es: ", promedio)