# Modificar un atributo

class Email:
    def __init__(self):  # definimos el constructor
        self.enviado = False  # agregamos el atributo por defecto

    def enviar_correo(self):  # definimos otra funcion para modificar el estadp por defecto
        self.enviado = True


mi_correo = Email()  # creamos el objeto y lo relacionamos con la clase 'Email()'
print(mi_correo.enviado)

mi_correo.enviar_correo()  # Relacionamos el objeto con el atributo modificador del estado por defecto
print(mi_correo.enviado)
