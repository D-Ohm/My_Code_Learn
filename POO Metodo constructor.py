# Metodo constructor

class Persona:
    pass

    def __init__(self, nombre, año):  # definimos el constructor
        self.nombre = nombre  # agregamos los atributos
        self.año = año

    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)  # con 'format' nos devuelve lo que queremos imprimir

    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)


doctor = Persona('JOSE', 26)  # creamos el objeto y lo relacionamos con la clase
print(doctor.descripcion())
print(doctor.comentario('hola que tal'))
