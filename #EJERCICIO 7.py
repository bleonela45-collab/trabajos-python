#EJERCICIO 7
#7. Una plataforma solicita al usuario ingresar un nombre de usuario. 
#El programa deberá: 
#• mostrar el nombre de usuario en mayúsculas;  
#• indicar la cantidad de caracteres que posee;  
#• informar cuántas vocales contiene;  
#• indicar si contiene algún espacio;  
#• mostrar un mensaje indicando si el nombre de usuario es válido, considerando que 
#debe tener entre 5 y 15 caracteres y no contener espacios. 

usuario = input("Ingrese su nombre de ususario: ")

mayus = usuario.upper()   #mayusculas
print("Nombre de mayúsculas: ", mayus)
print("Cantidad de caracteres:", len(usuario))

vocales = 0
for letra in mayus:
    if letra in "AEIOU":
        vocales = vocales + 1
print("Cantidad de vocales: ", vocales)

tiene_espacio = " " in usuario  #true si hay al menos un espacio
if tiene_espacio:
    print("Contiene espacios")
else:
    print("No contiene espacios")

if 5 <= len(usuario) <= 15 and not tiene_espacio:
    print("Nombre de usuario válido")
else:
    print("Nombre de ususario inválido")

