"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese 
número separados por comas.

"""

num = int(input("Introduce un número entero: "))
lista = []
for i in range(num):
    lista.append(i+1) 

print(lista)


for i in range(1, num+1, 2):
    print(i, end=", ")