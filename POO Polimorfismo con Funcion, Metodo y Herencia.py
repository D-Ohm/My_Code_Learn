# Polimorfismo con funcion

class Morron:
    def tipo(self):
        print('Verdura')
    
    def color(self):
        print('Rojo')


class Manzana:
    def tipo(self):
        print('Fruta')
    
    def color(self):
        print('Verde')


def funcion(objeto):  # Definimos la funcion que vincula los metodos e las dos clases anteriores con el objeto
    objeto.tipo()
    objeto.color()


nuevo_morron = Morron()
funcion(nuevo_morron)

nueva_manzana = Manzana()
funcion(nueva_manzana)

#Polimorfismo con metodos

class Venezuela:
    def c_natal(self):
        print('Caracas')
    
    def idioma(self):
        print('Español')


class Brasil:
    def c_natal(self):
        print('Rio')
    
    def idioma(self):
        print('Portugues')
        
venezolano = Venezuela()
brasilero = Brasil()

for pais in (venezolano,brasilero): # Usamos es el for para recorrer varias clases u objetos, ideal para muchas.
    
    pais.c_natal()
    pais.idioma()
    
# Polimorfismo con herencia

class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('Las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()