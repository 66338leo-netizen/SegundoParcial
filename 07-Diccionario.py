
alumno={
    "nombre":"Ana",
    "edad": 21,
    "carrera": "ingenieria"
}
print(type(alumno))
print(alumno)

print("print(alunmo['nombre'])= ",alumno["nombre"])
print("print(alumno.get('edad'))=",alumno.get('edad'))

alumno["promedio"] = 9.2
print(alumno)

alumno["edad"] = 22
print(alumno)

for clave in alumno:
    print(clave)
    print(clave,":",alumno[clave])

print("Cantidad de pares clave-valor; ",len(alumno))
print("claves del diccionario: ",alumno.keys())
print("valores del diccionario: ",alumno.values())
print("pares clave-valor: ",alumno.items())

