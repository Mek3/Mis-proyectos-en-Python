print("9) Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato ")
print("dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. ")
print ("Adaptar el programa anterior para que también funcione cuando el día o ")
print ("el mes se introduzcan con un solo carácter.\n")

fecha_nacimiento = input("Introduce tu fecha de naciemiento en formato dd/mm/aaaa: ")

tupla_aux = fecha_nacimiento.split("/")

print("Día: " + tupla_aux[0]) 
print("Mes: " + tupla_aux[1])
print("Año: " + tupla_aux[2])

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)