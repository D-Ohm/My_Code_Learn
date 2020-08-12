# Funciones II

# Creamos una funcion que genere numeros aleatorios

from random import *


def generaNumeroAleatorio(min, max):
    try:  # Usamos el try para generar una excepcion en caso de que 'min' sea mayor que 'max'
        if min > max:
            aux = min
            min = max
            max = aux
        return randint(min, max)
    except TypeError:
        print("Debes escribir numeros") #En caso de que se escriba una palabra en lugar de un numero
        return 0


i = 0
while i < 5:
    print(generaNumeroAleatorio(17, 10))
    i += 1
