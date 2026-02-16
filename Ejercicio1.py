
import os
ico=[]
alumno={
    "nombre":"",
    "edad": 0,
    "carrera": ""
}
i=0
os.system("cls")
cantidad=int(input("Cuantos alumnos se ingresaran: "))
for i in range(0,cantidad):
    a=input("Ingrese el nombre del alumno: ")
    b=int(input("Ingrese la edad del alumno: "))
    c=input("Ingrese la carrera del alumno: ")

    alumno["nombre"] = a
    alumno["edad"] = b
    alumno["carrera"] = c

    ico.append(alumno.copy())
    
print("Lista de alumnos ingresados: ")
for alumno in ico:
    print(alumno)