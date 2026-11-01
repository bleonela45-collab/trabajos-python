#EJERCICIO 3 - medi
# 3.  Durante un viaje, una persona desea llevar un registro de los gastos realizados. Para 
#cada gasto se ingresa el importe y una categoría (validar): 
#1 – Comida 
#2 – Transporte 
#3 – Entretenimiento 
#La carga de gastos finaliza cuando se ingresa un importe igual a 0. El importe no 
#puede ser negativo. 
#Al finalizar informar: 
#• el importe total gastado; 
#• el importe correspondiente a los gastos de comida; 
#• en que categoría se gastó más. 
#• el porcentaje de gastos de entretenimiento sobre el total de gastos realizados. 

total = 0
comida = 0
transporte = 0
entrenamiento = 0

importe = float(input("Ingrese importe de gasto ( 0 para finalizar )"))
while importe < 0:
    print ("El importe no puede ser negativo")
    importe = float(input("Ingrese importe de gasto ( 0 para finalizar)"))

while importe != 0:
    categoria = float(input("Ingrese categoria (1- Comida  2- Transporte  3- entrenamiento)"))

    while categoria < 1 or categoria > 3:
        print ("Categoria invalida")
        categoria = int(input("Ingrese categoria (1- Comida  2- Transporte  3- entrenamiento)"))

    total = total + importe

    if categoria == 1:
        comida = comida + importe 
    elif categoria == 2:
        transporte = transporte + importe
    else:
        entrenamiento = entrenamiento + importe

    importe = float(input("Ingrese importe del gasto (0 para finalizar)"))
    while importe < 0:
        print ("el importe no puede ser negativo")
        importe = float(input("Ingrese importe del gasto (0 para finalizar)"))

if comida > transporte and comida > entrenamiento:
    print("La categoria con mayor importe es COMIDAA")
elif transporte > comida and transporte > entrenamiento:
    print ("La categoria con mayor importe es TRANSPORTE")
elif entrenamiento > comida and entrenamiento > transporte:
    print ("La categoria con mayor importe es ENTRENAMIENTO")
else:
    print ("Hay 2 o mas categorias con el mismo importe")

if total > 0:
    porcentaje = entrenamiento * 100 / total
else:
    porcentaje = 0

print ("---REGISTRO DE GASTOS---")
print ("Toal comida: $", comida)
print ("Total transporte: $", transporte)
print ("Total entrenamiento: $", entrenamiento)
print ("Importe total: $", total)