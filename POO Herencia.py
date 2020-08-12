# Herencia

print('Ejemplo 1: Pokemones \n')


class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)


class Pikachu(Pokemon):  # Creo una subclase haciendo referencia a la clase padre
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre,
                                              tipoataque)  # Hago uso del atributo 'nombre' de la clase padre


class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)


nuevo_pokemon = Pikachu('"Pika"', 'Electrico')  # Creo el objeto 'nuevo_pokemon'
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Attack trueno'))

print(' \n')
print('Ejemplo 2: Calculadora \n')


class Calculadora:
    def __init__(self, numero):
        self.n = numero
        '''self.dato = [0 for i in range(numero)]'''  # valido que el codigo funciona igual sin esta linea
    # El ciclo 'for' acá sirve para determinar dentro de la funcion, la cantidad de datos a utilizar
    
    def ingresardato(self):
        self.dato = [int(input("Ingresar dato " + str(i + 1) + " = ")) for i in range(self.n)]


# Con el ciclo 'for' en esta linea, devolvemos el dato + 1 para volver a ingresarlo dentro del primer ciclo 'for'


class OpBasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)  # De esta forma podemos desde el metodo usar los atributos de la clase padre
        # Notar que el '2' es el 'self.n = numero' arriba que limita la cantidad de datos necesitados a dos datos
    
    def suma(self):
        a, b, = self.dato
        s = a + b
        print('El resultado es ', s)
    
    def resta(self):
        a, b, = self.dato
        r = a - b
        print('El resultado es ', r)
    
    def multi(self):
        a, b, = self.dato
        m = a * b
        print('El resultado es ', m)
    
    def div(self):
        a, b, = self.dato
        d = a / b
        print('El resultado es ', d)


class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)  # Lo mismo que en OpBasicas
    
    def cuadrada(self):
        import math  # Importo la blioteca math
        a, = self.dato
        print('El resultado es', math.sqrt(a))  # Hago uso de sqrt 'square root' de la boblioteca 'math'


objeto = OpBasicas()
print(objeto.ingresardato())
print(objeto.suma())

# objeto = raiz()
# print(objeto.ingresardato())
# print(objeto.multi())
print(isinstance(objeto, OpBasicas))
# funcion integrada que permite verificar la herencia,devuelve 'False' si no estamos trabajando con la clase mencionada
print(isinstance(objeto, Raiz))
# devuelve 'True' si estamos trabajando con la clase mencionada, sirve mas que nada, para verificar codigos muy largos
print(issubclass(OpBasicas, Calculadora))
# devuelve 'True' si la subclase mencionada pertence a la superclase mencionada, de lo contrario devuelve 'False'
