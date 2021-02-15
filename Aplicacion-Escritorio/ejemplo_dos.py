from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Probando")
lbl.grid(column = 0, row=0)

numero_columnas = 9
# Menos intuitiva pero mas eficiente
matriz = [None] * numero_columnas 
for i in range(numero_columnas):
    matriz[i] = [None] * numero_columnas 

text = (window)

for i in range(9):
    for j in range(9):
        lbl = Label(window, text="Probando")
        lbl.grid(column = i, row=j)
        matriz[i][j]= i*j

print(str(matriz))

window.mainloop()