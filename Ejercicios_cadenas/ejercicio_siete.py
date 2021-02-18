print("\n7) Escribir un programa que pregunte el correo electrónico del usuario en la consola")
print("y muestre por pantalla otro correo electrónico con el mismo nombre")
print("la parte delante de la arroba @) pero con dominio ceu.es.")

email = input("Introduce tu correo: ")
email_aux = email.split("@")
print(email_aux[0] + "@ceu.es")

print(email[:email.find('@')] + '@ceu.es')

