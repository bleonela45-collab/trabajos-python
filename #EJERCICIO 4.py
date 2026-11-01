#EJERCICIO 4
#ingresar cantidad de partidas
n = int(input("Ingrese la cantidad de partidas del Video Juegos: "))
i = 0

#crear vectir e inicializarlo
puntajes =  [0] * n

#cargar vector
for i in range(n):
    puntajes[i] = float(input("ingrese el puntaje de la partida ", + str(i + 1) + ": "))

#inicializar varibles
total = 0
mauores_500 = 0
menores_200 = 0

#buscar menor
menor = puntajes[0]
partida_menor = 1

#recorrer el vector
for i in range(n):
    #acumular puntajes
    total = total + puntajes[i]

    #contador puntajes mayores a 500
    if puntajes[i] > 500:
        mauores_500 = mauores_500 + 1

    #contar puntajes menos a 200
    if puntajes[i] < 200:
        menores_200 = menores_200 + 1

    #buscar menor puntaje
    if puntajes[i] < menor:
        menor = puntajes[i]
        partida_menor = i + 1

#calcular promedio
promedio = total / n

#calcular porentaje
porcentaje = menores_200 + 100 / 2 

#mostrar resultados
print()
print("RESULTADOS")
print("Puntaje total: ", total)
print("Puntaj promedio: ", promedio)
print("Menor puntaje: ", menor)
print("Partida en la que obtuvo el menor puntaje: ", partida_menor)
print("Cantidad de partidas con puntaje mayor a 500: ", mauores_500)
print("Porcentaje de partidas con puntaje menor a 200: ", menores_200)
print("Porcentaje de partidas con puntaje menor a 200: ", porcentaje, "%")