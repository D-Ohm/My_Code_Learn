# f - string
# format %

curso = 'Python'
print("Tutoriales de % s" % curso)

nombre = 'Demian'
edad = '37'
print("Hola soy % s y tengo % s años." % (nombre, edad))
print("Hola soy {} y tengo {} años.".format(nombre, edad))
print(f"Hola soy {nombre} y tengo {edad} años.")
'''Tres formas de lograr lo mismo a la hora de mostrar por pantalla las variables'''


# Para el caso de la POO

class Estudiante:
    def __init__(self, nombre1, apellido, edad1):
        self.nombre = nombre1
        self.apellido = apellido
        self.edad = edad1
    
    def __str__(self):  # Para mostrar por pantalla de forma INFORMAL los datos de la clase que quiero traer
        return f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años."


nuevo_estudiante = Estudiante('Demian', 'Ovejero', 37)
print(f"{nuevo_estudiante}")


class Estudiante2:
    def __init__(self, nombre2, apellido, edad2):
        self.nombre = nombre2
        self.apellido = apellido
        self.edad = edad2
    
    def __repr__(self):  # Para mostrar por pantalla de forma FORMAL los datos de la clase que quiero traer
        return f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años."


nuevo_estudiante = Estudiante2('Demian', 'Ovejero', 37)
print(f"{nuevo_estudiante !r}")
