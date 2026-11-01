#ejercicio 1 - rep
#1.  Un centro deportivo está organizando nuevas actividades y necesita registrar los datos 
#de las personas que desean participar. Desarrolle un programa en Python que permita 
#ingresar la información de una persona. 
#El programa deberá solicitar: 
#• Nombre y apellido. 
#• Edad. 
#• Altura expresada en metros. 
#• Peso expresado en kilogramos. 
#A partir de estos datos, deberá: 
#• Mostrar un mensaje de bienvenida utilizando el nombre y apellido. 
#• Calcular y mostrar la edad que tendrá la persona dentro de 5 años. 
#• Calcular y mostrar el índice de masa corporal (IMC), utilizando la fórmula: 
#IMC = peso / altura² 
#• Mostrar los datos ingresados junto con los resultados obtenidos. 

print("------- DATOS PERSONALES --------")

nombre_apellido = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese EDAD: "))
altura = float(input("Ingrese su estatura (metros): "))
peso = float(input("Ingrese su peso (kilogramos): "))

print()
print("BIENVENIDO/A ", nombre_apellido)
print("Datos ingresados: ")
print("Nombre y apellido: ", nombre_apellido)
print("Edad: ", edad)
print("Altura: ", altura)
print("Pes: ", peso)

edad2 = edad + 5
print("En 5 años ", nombre_apellido, "tendrá: ", edad2)

IMC = peso / altura ** altura
print("IMC: ", IMC)