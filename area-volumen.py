pi = 3.14
radio = float(input("Ingrese el radio del circulo: "))
altura = float(input("Ingrese la altura del cilindro: "))
AL = 2 * pi * radio * altura
B = pi * radio ** 2
AT = AL + 2 * B
VOLUMEN = B * altura
print("El area total es: ", AT)
print("El vomunen es: ", VOLUMEN)
