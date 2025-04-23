"""
1. Encuesta gustos musicales de n personas
2. ingresar edad y preferencia
3. Cantidad de adultos que prefiren el Rock
4. Menores de edad que prefieren el Pop
5. Adultos mayores que prefieren Jazz o Folclore
6. Porcentaje de adultos que prefieren todo menos Pop
"""

n = int(input("Cantidad de personas "))
rock = 0; pop = 0; amayor = 0; npop = 0; 
for i in range(n):
    edad = int(input("Ingrese su edad "))
    print("Seleccione: ")
    print("""
        1. Rock
        2. Pop
        3. Jazz
        4. Folclore
    """)
    
    op = int(input("Ingrese su opción "))
    if edad >= 18: 
        if op == 1:
            rock += 1
    else:
        if  op == 2:
            pop += 1
    if edad >= 65:
        if op == 3 or op == 4:
            amayor += 1 
    if edad >= 18:
        if op != 2:
            npop += 1

porc = npop / n 
print("Cantidad de adultos que prefiren el Rock ", rock)
print("Menores de edad que prefieren el Pop ", pop)
print("Adultos mayores que prefieren Jazz o Folclore ", amayor)
print("Porcentaje de adultos que prefieren todo menos Pop ", porc * 100, "%")