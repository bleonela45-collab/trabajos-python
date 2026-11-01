#EJERCICIO 1
"""1.- Una empresa registra los códigos de los productos que ingresan a un depósito. Los 
códigos se almacenan en una pila, de manera que el último producto ingresado es el 
primero que puede retirarse. 
Ingresar la cantidad de productos, que debe ser menor a 30, y cargar sus códigos en una 
pila. Luego: 
a) Mostrar la cantidad de productos almacenados. 
b) Mostrar el código del producto que se encuentra en el tope de la pila. 
c) Retirar y mostrar los productos de la pila, respetando el orden de salida. """

def apilar(pila, dato):
    pila.append(dato)
def tope (pila):
    return pila[-1]
def pila_vacia(pila):
    return len(pila)==0
def desapilar(pila):
    return pila.pop()

pila = []
N = int(input("Ingrese la cantidad de productos: "))
while N <= 0 or N >= 30:
    N = int(input("Cantidad incorrecta. Ingrese nuevamente (Cantidad > 30)"))

for i in range(N):
    codigo = int(input("Ingrese el codigo de producto: "))
    apilar(pila, codigo)

print ("Cantidad de productos: ", len(pila))
print ("Producto en el tope: ", tope(pila))

print ("Producos retirados: ")
while not pila_vacia(pila):
    codigo = desapilar(pila)
    print (codigo)