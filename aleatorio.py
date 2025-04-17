# Adivina un número entre 1 y 10 - 5 intentos 

import random
nro = random.randint(1,100)

i = 1;intento=0
while i != 0:
    print("Adivina un número entre 1 y 100 - 10 intentos ") 
    num =int(input("Ingerese un número "))
    intento+=1 # intento = intento + 1
    print("Intente Nro ", intento)
    if num==nro:
        print("Felicitanciones adivinaste!!! ")
        break
    elif num > nro:
        print("El número es menor")
    else:
        print("El neumero es mayor")
    # if intento==5:
    #     print("Perdiste mas de 5 intentos!!! ")

    if intento == 10:
        print("Perdiste mas de 10 intentos!!!")