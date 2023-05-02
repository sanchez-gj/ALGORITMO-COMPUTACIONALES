catetoOpuesto = float(input("Ingrese el cateto opuesto: "))
catetoAdyacente = float(input("Ingrese el cateto adyacente: "))
hipotenusa = (catetoOpuesto**2 + catetoAdyacente**2)**(1/2)
print("La hipotenusa es: " +  str(round(hipotenusa, 2)))
