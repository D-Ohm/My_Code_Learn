# Tkinter Imagenes

from tkinter import *

raiz = Tk()
raiz.title("Ventana de imagen")


MiFrame = Frame(raiz, width=750, height=400,)
MiFrame.pack()

MiImage = PhotoImage(file="avatar_ani1.GIF")
Label(MiFrame, image=MiImage).place(x=272, y=225)

raiz.mainloop()
