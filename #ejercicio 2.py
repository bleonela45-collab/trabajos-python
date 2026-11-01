#ejercicio 2
#2. Una plataforma deportiva permite a los usuarios registrarse para participar de sus 
#actividades. Para completar el registro, la persona debe ingresar un nombre de usuario y 
#una contraseña. 
#El programa deberá solicitar: 
#• Nombre de usuario. 
#• Contraseña. 
#• Reingreso de la contraseña. 
#Para que el registro sea válido, la contraseña debe cumplir con las siguientes condiciones: 
#• Tener al menos 6 caracteres. 
#• Coincidir con la contraseña ingresada anteriormente. 
#El programa deberá informar: 
#• “Registro realizado correctamente”, mostrando además el nombre de usuario, si 
#se cumplen ambas condiciones. 
#• “La contraseña debe tener al menos 6 caracteres”, si no cumple con la longitud 
#mínima. 
#• “Las contraseñas no coinciden. Intente nuevamente”, si las contraseñas son 
#diferentes. 

print("Bienvenido al sistema")
usuario = input("Ingrese nombre de usuario")

while True:
    contraseña1 = input("Ingrese una contraseña: ")
    contraseña2 = input("Reeingrese la contraseña: ")

    if len(contraseña1) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
    elif contraseña1 != contraseña2:
        print("Las contraseñas no coinciden. Intentelo nuevamente.")
    else: 
        print("Registro relizado correctamente. Usuario: ", usuario)
        break
