# Polimorfismo

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tipo_animal(self):
        pass


class Leon(Animales):
    def tipo_animal(self): # Esta sublcase usa un metodo del mismo nombre que el metodo de la superclase
        print("Animal salvaje")


class Perro(Animales):
    def tipo_animal(self): #En este caso lo mismo, pero con dieferente valor
        print("Animal doméstico")


nuevo_animal = Leon('Simba')
nuevo_animal.tipo_animal()

nuevo_animal2 = Perro('Lasie')
nuevo_animal2.tipo_animal()
