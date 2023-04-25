# Calcular cuantas letras tiene el nombre ingresado
# 1. Pedir el nombre
# 2. Contar las letras
# 3. Imprimir el resultado
nombre = input("Ingrese su nombre: ")
print("Su nombre tiene", len(nombre), "letras")


#-------------------#
# Introducir un numero y decir si es par o impar
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#-------------------#
# Pregundar si es hombre o mujer
genero = input("Ingrese su genero (Hombre/Mujer): ")
if genero == "Hombre":
    print("Usted es un hombre")
elif genero == "Mujer":
    print("Usted es una mujer")
else:
    print("Genero no valido")
#-------------------#
#Señalar la hora
hora = int(input("Ingrese la hora: "))
if hora >= 0 and hora <= 12:
    print("Buenos dias")
elif hora >= 13 and hora <= 19:
    print("Buenas tardes")
elif hora >= 20 and hora <= 24:
    print("Buenas noches")
else:
    print("Hora no valida")

