"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en 
la inversión cada año que dura la inversión.

"""

cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual: "))
num_anyos = int(input("Introduce el número de años: "))

for i in range(num_anyos):
    benificio_anual = (interes_anual/100) * cantidad_invertir
    cantidad_invertir = cantidad_invertir + benificio_anual
    print("Año: " + str(i+1) + " Cantidad ganada: "+ str(cantidad_invertir))
    



