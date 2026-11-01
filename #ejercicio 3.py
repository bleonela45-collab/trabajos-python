#ejercicio 3
'''5.- Dada una pila que almacena un número de n dígitos mostrar el mensaje “el número es 
capicúa” en caso de que el número almacenado así lo sea, caso contrario mostrar el mensaje 
“el número no es capicúa”.  '''

def apilar(pila, dato):
    pila.append(dato)
def desapilar(pila):
    return pila.pop()
def pila_vacia(pila):
    return len(pila)==0
def tope(pila):
    return pila[-1]

pila1=[]
pila2=[]

N = input("Ingrese un numero: ") #numero como cadena de carac
for i in range(len(N)):
    apilar(pila1, N[i])
    apilar(pila2, N[len(N) - 1- i]) #pila invertida

capicua = True

while not pila_vacia(pila1):
    digito1 = desapilar(pila1)
    digito2 = desapilar(pila2)
    if digito1 != digito2:
        capicua=False

if capicua:
    print("El numero es capicua")
else:
    print("El numero no es cap")