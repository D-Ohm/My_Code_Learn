# Metodos

# Un metodo es una funcion que esta dentro de una clase, dterminan una accion o un comportamiento


class Matematica:
    def suma(self):  # Nombre del metodo, el nombre por lo general indica accion
        self.n1 = 2  # SELF hace referencia al objeto (aun no creado y al colocarse en esta linea busca ejecutar el #metodo
        self.n2 = 3


s = Matematica()  # s viene a ser el ID del objeto
s.suma()  # llamamos al objeto y luego al metodo
print(s.n1 + s.n2)


# Otra forma de llamar a un metodo
print('\n')
class Ropa:
    def __init__(self):
        self.marca = 'Nike'
        self.talla = 'M'
        self.color = 'rojo'


camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

#Ejercicio de calculadora con POO
print('\n')
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2


operacion = Calculadora(10, 5)
print(operacion.suma)
