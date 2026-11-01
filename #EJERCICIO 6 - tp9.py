#EJERCICIO 6
def encolar(cola, dato):
    cola.append(dato)

def desencolar(cola):
    return cola.pop(0)

def frente(cola):
    return cola[0]

def cola_vacia(cola):
    return len(cola) == 0

#ingreso de solicitudes
def ingreso (asientos):
    s = 0
    n = 1

    while n != 2 and s < asientos:
        print("1. Comprar entrada")
        print("2. Salir")

        n = int(input("Ingresas opción: "))

    if n == 1:
        entrada = int(input("Ingrese la cantidad de entradas a comprar: "))

        while entrada > asientos - s:
            entrada = int(input("Asientos insuficientes. Ingresar cantidad de entradas a comprar: "))

        if entrada > 0:
            encolar(cola, entrada)
            s = s + entrada

        if s == asientos:
            print("Entradas agotadas.")

def proceso(precio, asientos):
    cantpers = 0
    enttotal = 0
    monto_total = 0

    while not cola_vacia(cola):
        entrada = desencolar(cola)

        cantpers += 1
        enttotal += entrada
        monto_total += (entrada * precio)

    entradas_sobrante = asientos - enttotal

    print("Cantidad de personas que compraron entradas: ", cantpers)
    print("Cantidad total de entradas vendidas: ", enttotal)
    print("Monto total recsudado: ", monto_total)
    print("Cantidad de entradas sobrantes: ", entradas_sobrante)


#programa principal
cola = []

cantasientos = int(input("Ingrese la cantidad de asientos de la sala: "))
precio = float(input("Ingrese el precio de las entradas: "))

print("\nCarga de bolteria ...")

ingreso(cantasientos)
proceso(precio, cantasientos)