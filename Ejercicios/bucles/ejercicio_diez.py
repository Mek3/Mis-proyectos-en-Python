"""
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no.

"""
num = int(input("Introduce un número: "))
ok = True
num_divisor = int(num/2) + 1
i = 2

while ok:
    res = num%i
    if res == 0:
        ok = False
        print("El número "+ str(num) + " no es primo ")
    elif i < num_divisor:
        i = i+1
    else : 
        ok = False
        print("El número "+ str(num) + " es primo ")


n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")