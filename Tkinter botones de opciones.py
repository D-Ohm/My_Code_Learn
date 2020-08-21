# Tkinter botones de opciones

from tkinter import *

raiz = Tk()

opcion=IntVar()

def imprimir():
    print(opcion.get())
    if opcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
    else:
        etiqueta.config(text="Has legido Femenino")

Label(raiz, text="Seleccione su genero:")

Radiobutton(raiz, text="Masculino", variable=opcion, value= 1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=opcion, value=2,  command=imprimir).pack()

etiqueta=Label(raiz)
etiqueta.pack()

raiz.mainloop()