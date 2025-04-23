"""
1. El pago base es de $220.000 considerando los primeros 100 km.
2. Si la distancia es mayor a 100 km. y menor a 250 km. se cobra $280.000
3. Si la distancia es mayor a 250 km. Se cobra $900 por cada km, más el pago base.
4. Si la cantidad de estudiantes que viaja es mayor a 45 se le agrega un 70% del costo obtenido.
5. Considerar agregar $3500 para colación por cada estudiante. 
6. Se debe mostrar el costo total de la salida a terrero.  
"""

km = int(input("Km del viaje "))
es = int(input("Cantidad de estudiantes "))

if km <= 100: 
    t = 220000
elif km <= 250:
    t = 280000
else:
    t = (900 * km) + 220000

if es > 45: 
    tarifa = (t * 1.7)    # Tarifa = t + (t * 0.7)
else:
    tarifa = t 

colacion = es * 3500

print(f"Costo del viaje ${tarifa} gasto colacion ${colacion} Total salida a tereno  ${tarifa + colacion}")
# print(f"Costo del viaje", (tarifa), "gasto colacion", (colacion), "Total salida a tereno",  (tarifa + colacion)")