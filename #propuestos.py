#propuestos
'''. Se desea facturar el consumo del abono de un teléfono. Para ello se informa la tarifa 
por segundo y la duración expresada en horas, minutos y segundos. Como resultado se 
debe informar la duración en segundos de cada comunicación y su costo. '''

print("====== FACTURA DE CONSUMO =====")
tarifa = float(input("Ingrese el valor de la tarifa por segundo: "))

print("Ingrese la duración (0, 0, 0 para finalizar)")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_seg = horas * 3600 + minutos * 60 + segundos

while total_seg != 0:
    costo = total_seg * tarifa
    print("Duración en segundos:", total_seg)
    print(f"Costo: ${costo:.2f}")

    print("Ingrese la duración (0, 0, 0 para finalizar)")
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    total_seg = horas * 3600 + minutos * 60 + segundos

