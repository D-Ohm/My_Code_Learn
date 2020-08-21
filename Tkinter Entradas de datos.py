# Tkinter Entrada de datos

from tkinter import *

Raiz = Tk()
Raiz.title("Ingrese sus datos")

miFrame = Frame(Raiz, width=800, height=550)
miFrame.pack()

miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre)
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
cuadroComent = Text(miFrame, width=26, height=5)
cuadroComent.grid(row=4, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=cuadroComent.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")
cuadroComent.config(yscrollcommand=scrollVertical.set)

nombreLabel = Label(miFrame, text="Nombre:")
# nombreLabel.place(x=100, y=100)
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
DNILabel = Label(miFrame, text="DNI:")
DNILabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
psswLabel = Label(miFrame, text="Contraseña:")
psswLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
comentLabel = Label(miFrame, text="Comentario:")
comentLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


def codigoBottom():
    miNombre.set('Demian')


botonEnvio = Button(Raiz, text="Enviar", command=codigoBottom)
botonEnvio.pack()

Raiz.mainloop()
