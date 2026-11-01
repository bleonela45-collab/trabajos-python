#ejercicio 2 tp9
"""2.- Una aplicación almacena en una pila N acciones realizadas por un usuario. Cada acción 
está representada por un número entero. 
Ingresar la cantidad de acciones y cargar la pila. 
Luego, solicitar dos valores X e Y y reemplazar por Y todas las acciones cuyo valor sea 
igual a X. 
Al finalizar, mostrar la pila resultante e informar si se realizó algún reemplazo. """

def apilar(pila, dato):
    pila.append(dato)
def desapilar(pila):
    return pila.pop()
def pila_vacia(pila):
    return len(pila)==0
def tope(pila):
    return pila[-1]

pila = []
aux = []

N = int(input("Ingrese la cantidad de acciones: "))
while N <= 0:
    N = int(input("Cantidad incorrecta. Ingrese nuevamente (Cantidad Numero Entero): "))

for i in range(N):
    accion = int(input("Ingreses el numero de acción: "))
    while accion < 0:
        accion = int(input("Accion incorrecta. Ingrese nuevamente (numero entero): "))
    apilar(pila, accion)

x = int(input("ingrese un valor para x: "))
y=int(input("Ingrese un valor para y: "))

band=0
while not pila_vacia(pila):
    accion=desapilar(pila)
    if x == accion:
        accion = y
        band=1
    apilar(aux, accion)

while not pila_vacia(aux):
    accion=desapilar(pila)
    apilar(pila, accion)

if band==1:
    print("Hubo cambios en la pila.")
    while not pila_vacia(pila):
        temp=desapilar(pila)
        print(accion)
else:
    print("No se realzaron cambios")
    while not pila_vacia(pila):
        temp=desapilar(pila)
        print(accion)