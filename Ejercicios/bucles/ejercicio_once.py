"""
Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de 
la palabra introducida empezando por la última.

"""
palabra = input("Introduce un palabra cualquiera: ")
for i in range(len(palabra)-1, -1, -1):
    print(str(palabra[i]), end=", ") 


