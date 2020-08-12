# Metodo de clase y estatico

# Metodo de clase @classmethod
class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    def __repr__(self):
        return f"Pastel ({self.ingredientes !r})"
    
    @classmethod
    def pastel_chocolate(cls):
        # notamos que se trata de un metodo independiente del constructor, aunque este dentro de la clase
        
        return cls(['Harina', 'Leche', 'Chocolate'])
    
    @classmethod
    def pastel_vainilla(cls):
        return cls(['Harina', 'Leche', 'Vainilla'])


print(Pastel.pastel_chocolate())

# Metodo estatico @staticmethod

import math


# noinspection NonAsciiCharacters,NonAsciiCharacters
class Pastel2:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    
    def __repr__(self):
        return f'Pastel({self.ingredientes}, 'f'{self.tamaño})'
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    # noinspection NonAsciiCharacters
    @staticmethod
    def tamaño_area(A):
        # Puedo colocar cualquier referencia como parametro, no necesariamente 'self' como en los metodos clasicos.
        return A ** 2 * math.pi


nuevo_pastel = Pastel2(['Harina', 'Leche', 'Huevo', 'Azucar'], 4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_area(4))
