# Tkinter Entrada de datos

from tkinter import *

Raiz = Tk()
Raiz.title("Ingrese sus datos")

miFrame = Frame(Raiz, width=800, height=450)
miFrame.pack()

cuadroNombre = Entry(miFrame)
# cuadroNombre.place(x=100, y=100)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="center")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido.config(fg="blue", justify="center")
cuadroDNI = Entry(miFrame)
cuadroDNI.grid(row=2, column=1, padx=10, pady=10)
cuadroDNI.config(fg="blue", justify="center")
cuadroPssw = Entry(miFrame)
cuadroPssw.grid(row=3, column=1, padx=10, pady=10)
cuadroPssw.config(fg="blue", justify="center")
cuadroPssw.config(show="*")

nombreLabel = Label(miFrame, text="Nombre:")
# nombreLabel.place(x=100, y=100)
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
DNILabel = Label(miFrame, text="DNI:")
DNILabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
psswLabel = Label(miFrame, text="Contraseña:")
psswLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

Raiz.mainloop()
