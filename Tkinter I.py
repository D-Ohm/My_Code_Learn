# Tkinter I

from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba")
#  raiz.resizable(False, False)
#  raiz.geometry("650x350")
raiz.config(bg="yellow")  # "bg" es por background
#  raiz.iconbitmap('~/Documents/Cursos/CursoPython/Imagenes Py/Iconos/snowflake-4-64.ico')


MiFrame = Frame()
MiFrame.pack(fill="x", expand="True", anchor="n")
'''Se puede usar 'side = "left" ó "right" o "top" o "bottom"' por ejemplo, en lugar de 'fill', para ubicar el recuadro
a un lado de la ventana. Se puede 'anchor ="n"' para ubicar al norte "s" para sur, "e" para este y "w" para oeste'''
MiFrame.config(bg="blue")
MiFrame.config(width="650", height="350")
MiFrame.config(bd=10)  # "bd" es por bordes
MiFrame.config(relief="sunken")  # "relief" refiere al relieve, otra opcion puede ser ta,bien 'groove', googlear +
MiFrame.config(cursor="box_spiral")

raiz.mainloop()

