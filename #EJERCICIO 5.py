#EJERCICIO 5
#5. En una localidad nos piden que realicemos un análisis de las lluvias caídas en un 
#semestre. Desarrolle un programa que permita ingresar por teclado la cantidad de 
#milímetros de lluvia caída en cada uno de los 6 meses del semestre y almacenar estos 
#datos en un vector. 
#Una vez cargados todos los datos en el vector, realizar un recorrido para analizarlos y 
#obtener la siguiente información: 
#a) El promedio de milímetros de lluvia caídos durante el semestre. 
#b) La cantidad de meses en los que la lluvia caída fue mayor o igual al promedio. 
#c) El número del mes en el que se registró la menor cantidad de lluvia y los 
#milímetros caídos en dicho mes. 
#d) La cantidad total de milímetros de lluvia caída durante los primeros 3 meses del 
#semestre. 
#e) Si dicho mes tuvo 0 mm caídos indicar con un mensaje. 

lluvias =[]
print("Analisi de lluvias en un semestre \n")

#ingresar lluvias del sementres
for mes in range(6):
    dato = float(input(f"Ingrese los mm de lluvia del {mes} mes"))
    lluvias.apped (dato)

print("lluvias", lluvias)

#calcular promedio de mm caidso del trimestre
suam = 0
for mes in lluvias:
    suam = suam + mes
promedio = suam/len(lluvias) #6

#mostrar promedio de mm caidos en el trismertes
print(f"Promedio de llvuias caidas: {promedio:.2f}")     #acordarse la f para mostrar el "resulado"

mayores_promedio = 0
#cantidad de meses con mas o igual lluvia que el promedio
#mes con menos lluvia en el trimestre
tresmese = 0
for mes in range (6):
    if(lluvias [mes] >= promedio):
        mayores_promedio+=1
    if mes == 0:
        menor = lluvias[mes]
        masmenor = mes + 1
    if menor > lluvias[mes]:
        menor =lluvias[mes]
        masmenor = mes+1
    if(mes<3):
        tresmese = tresmese + lluvias[mes]
    if lluvias[mes] == 0:
        print(f"El mes {mes + 1} tiene 0 mm")

print("Meses con lluvias mayores al promedio: ", mayores_promedio)

if menor == 0:
    print(f"El mes menor {masmenor} hubo 0mm")
else:
    print(f"El mes {masmenor} tuvo la menor cantudad de lluvia con: {menor}mm")

print("La lluvia caida en los primero 3 meses es: ", tresmeses)