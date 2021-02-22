print("Escribir un programa que pregunte por consola por los productos de una cesta ")
print("de la compra, separados por comas, y muestre por pantalla cada uno de los productos ")
print("en una línea distinta.\n")

lista_compra = input("Introduce la lista de la compra: ")
tupla = lista_compra.split(",")
for t in tupla:
    print(t)

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

print('\n'.join(cesta.split(',')))