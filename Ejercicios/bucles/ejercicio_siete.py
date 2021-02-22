"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

"""

for i in range(10):
    print("\n Tabla de multiplicar del " + str(i+1))
    for j in range(10):
        print(str(i+1) + " X " + str(j+1) + " = " + str((i+1)*(j+1)))


for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")