#ejercicio 1
print ("====== DATOS PERSONALES =======")

nombre_apellido = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
altura = float(input("Ingrese la altura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))


print("==== BIENVEIDO/A ====", nombre_apellido, "---")
      
#edad luego de 5 años
edad2 = edad + 5
print("La edad que tendra: ", nombre_apellido, "en 5 años es: ", edad2)

#IMC
imc = peso / (altura ** 2)
print("El indice de masa corporal (IMC) de ", nombre_apellido, "es de: ", imc)

print("====== DATOS INGRESADOS Y OBTENIDOS ======")
print("NOMBRE: ", nombre_apellido)
print("EDAD: ", edad)
print("ALTURA: ", altura)
print("PESO: ", peso)

print("====== DESPUES DE 5 AÑOS =====")
print("EDAD EN 5 AÑOS: ", edad2)
print("")
