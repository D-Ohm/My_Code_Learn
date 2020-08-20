# Tkinter I

from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba")
#  raiz.resizable(False, False)
#  raiz.geometry("650x350")
raiz.config(bg="yellow")  # "bg" es por background

MiFrame = Frame(raiz, width=750, height=400, )
MiFrame.pack(fill="x", expand="True")
'''Se puede usar 'side = "left" ó "right" o "top" o "bottom"' por ejemplo, en lugar de 'fill', para ubicar el recuadro
a un lado de la ventana.'''
MiFrame.config(bg="lightblue")
# MiFrame.config(width="650", height="350")
MiFrame.config(bd=10)  # "bd" es por bordes
MiFrame.config(relief="sunken")  # "relief" refiere al relieve, otra opcion puede ser ta,bien 'groove', googlear +
MiFrame.config(cursor="box_spiral")

Label(MiFrame, text="Hola Mundo", fg="black", font=("Monaco", 30)).place(x=75, y=325, anchor="w")
'''Se puede anchor ="n" (12 en el reloj) para orientar al norte "s" (6 en el reloj)
 para sur, "e" (9 en el reloj)  para este y "w" (3 en el reloj) para oeste'''

raiz.mainloop()
