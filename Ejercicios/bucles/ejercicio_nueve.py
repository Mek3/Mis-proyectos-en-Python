"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""
ok = True
while ok:
    password = input("Introduce la contraseña: ") 
    if password == "yuho":
        ok = False
        print("Contraseña correcta.")
    else :
        print("La contraseña es errónea.")


key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")



