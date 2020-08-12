# Herencia multiple

class Telefono:
    def __init__(self):
        pass
    
    def llamar(self):
        print('Llamando...')
    
    def ocupado(self):
        print('ocupado...')


class Camara:
    def __init__(self):
        pass
    
    def fotografia(self):
        print('fotofrafiando...')


class Reproduccion:
    def __init__(self):
        pass
    
    def musica(self):
        print('Reproduciendo audio...')
    
    def video(self):
        print('Reroduciendo video...')


class Smartphone(Telefono, Camara, Reproduccion): # Herencia multiple
    def __del__(self):
        """ Si "__init__" es el constructor, "__del__" es el destructor, sirve para destruir la
        clase una vez usada y asi liberar recursos."""
        print('Telefono apagado')


movil = Smartphone()
print(dir(movil))  # Sirve para verificar las opciones que tengo disponibles para trabajar este objeto
print(movil.video())
