print("\n8) Escribir un programa que pregunte por consola el precio de un producto en euros") 
print("con dos decimales y muestre por pantalla el número de euros y ")
print("el número de céntimos del precio introducido.\n")

importe = input("Introduce el precio del producto: ")
print(importe[:importe.find(",")] + " euros y "+ importe[importe.find(",")+1:] + " céntimos.")
