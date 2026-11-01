#EJERCICIO 6
#6. Desarrollar un programa que permita procesar los datos del último censo de una 
#pequeña población. Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos 
#finaliza al ingresar cualquier otro valor para sexo. El programa debe informar: 
#a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser 
#igual) 
#b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive) 
#c) Si existe por lo menos un varón que supere los 85 años mostrar un mensaje “Existe 
#al menos un varón mayor a 85 años”

print("=== SISTEMA DEL CENSO ===")
print('*' * 80)

#inicializar contadores y acumuladores
varones = 0
mujeres =0 
escolares = 0
mayor_85 = False

#primera carga de datos de corte antes del ciclo
sexo = input("ingrese sexo (M/F - otro valor termina): ")
#proceso repetitivo
while sexo == 'M' or sexo == 'F':
    edad = int(input("Ingrese edad: "))

    if sexo == 'M':
        varones = varones + 1
        if edad >85:
            mayor_85 = True
    else:
        mujeres = mujeres + 1
        if 4 <= edad <= 18:
            escolares = escolares + 1

    sexo = input("Ingrese sexo (M/F - otro valor termina: )").upper()

#aparatado a
if mujeres > varones:
    print("La mayor cantidad corresponde a Mujeres.")
elif mujeres < varones:
    print("La mayor cantidad corresponde a Varones")
if mujeres == varones:
    print("Hay la misma cantidad de mujeres y varones")

#aparatado b
print("La cantidad de escolares es: ", escolares)

#apartado c
if mayor_85:
    print("Existe al menos un varon mayor a 85 años.")

