# Funciones para atributos

class Persona:
    edad = 27
    nombre = 'victor'
    pais = 'brasil'


doctor = Persona()
print('la edad es: ', doctor.edad)

print('la edad es: ', getattr(doctor, 'edad'))  # Llamamos directamente al atributo

print('el doctor tiene una edad?', hasattr(doctor, 'edad'))
print('el doctor tiene un apellido?', hasattr(doctor, 'apellido'))
# TODO: ver como funciona

print('antes era: ', doctor.nombre)
setattr(doctor, 'nombre', 'hector')  # cambio el valor de un atributo
print('ahora se llama:', doctor.nombre)
# OPTIMIZE: Excelente, ya se como funciona TODO PAPA!! :D

delattr(Persona, 'pais')  # para borrar un atributo de la funion
print('tenemos el pais de origen del doctor?:', hasattr(doctor, 'pais'))
