"""
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

"""

num = int(input("Introduce un número entero: "))

for i in range(num):
    print(str(num-i ), end=", ")


