"""
Escribir un programa en el que se pregunte al usuario por una frase 
y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase.

"""
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
cont = 0

for i in frase:
    if i == letra:
        cont+=1

print(cont)