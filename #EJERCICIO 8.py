#EJERCICIO 8
#8. Ingresar Una empresa desea analizar los ingresos obtenidos por uno de sus vendedores 
#durante el primer semestre del año. 
#Desarrollar un programa en Python que permita: 
#• Cargar en un vector los sueldos correspondientes a los meses de enero a junio. 
#• Mostrar los sueldos registrados indicando el mes correspondiente. 
#• Determinar el sueldo más alto del semestre y el mes en que fue recibido. 
#• Calcular el sueldo promedio del período. 
#• Calcular el aguinaldo, correspondiente a la mitad del sueldo más alto del semestre. 
#• Generar un nuevo vector que contenga la diferencia entre cada sueldo y el sueldo 
#promedio. 

print("===== SISTEMA DE LA EMPRESA =====")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
sueldos = []

#cargar: pedir un sueldo por cada mes
for i in range(6):
    s = float(input("Ingrese el sueldo de " + meses[i] + ": "))
    sueldos.append(s)

#mostrar sueldos con su mes
for i in range(6):
    print(meses[i], ":", sueldos[i])

#sueldo ams alto y su mes
mayor = sueldos[0]
pos = 0

for i in range(6):
    if sueldos[i] > mayor:
        mayor = sueldos[i]
        pos = i

print("Sueldo más alto: ", mayor, "en", meses[pos])

#promedio
suma = 0
for i in range(6):
    suma = suma + sueldos[i]

promedio = suma / 6
print(f"Sueldo promedio: {promedio:.2f}")

#Aguinaldo
aguinaldo = mayor / 2
print(f"Aguinlado: {aguinaldo:.2f}")

#neuva lista con diferencias
diferencias = []
for i in range(6):
    diferencias.append(sueldos[i] - promedio)

for i in range(6):
    print(f"{meses[i]}: {diferencias[i]:.2f}")