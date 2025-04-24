"""Instrucciones: 
1. Calcular los promedios de n notas de n alumnos
2. Mostrar promedio de cada alumno
3. Mostrar promedio del curso y el nombre del alumno con mejor promedio
"""

n = int(input("ingrese la cantidad de alumnos: "))
sum_prom = 0; mayor = 0

for i in range(1, n + 1 ):
    nombre = input("Ingrese su nombre: " + str(i))
    notas = int(input("Ingrese cantidad de notas: "))
    sum_nota = 0
    for j in range(notas):
        nota = float(input("Ingrese la nota ")) 
        sum_nota += nota 
    prom = sum_nota / notas # Promedio de notas 
    print("Promedio Notas de: ", nombre, " ",prom)
    sum_prom += prom # Promedio del curso
    if prom > mayor: 
        mayor = prom
        nom = nombre


promedio_curso = sum_prom / n
print("Promedio del curso: ", promedio_curso)
print("Alumno con mejor promedio: ", nombre)


