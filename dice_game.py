# Dados: ingresar N jugadores y cada uno tira 3 veces el dado. Gana el que suma más puntos 
import random 
n = int(input("Ingrese cantidad de jugadores "))
for i in range(1, n+1):
    print("=====================")
    print("Jugador ", i)
    j = 1 ; ac = 0
    while j < 4:
        nro = random.randint(1,6)
        print("Tiro ", nro)
        ac += nro
        j += 1
    print("Total puntos: ", ac)
