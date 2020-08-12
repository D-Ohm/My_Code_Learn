# Herencia


class Persona:
    def __init__(self):
        self.nombre = str(input("Ingrese nombre: "))
        self.edad = int(input('Ingrese edad: '))
    
    def imprimir_datos(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"


class Empleado(Persona):
    
    remuneracion: int

    def sueldo(self):
        
        self.remuneracion = int(input("Ingrese sueldo: "))
        
        if self.remuneracion > 3000:
            print(f'{self.nombre} paga impuesto')
        else:
            print(f'{self.nombre} no paga impuesto')


nueva_persona = Persona()
print(nueva_persona.imprimir_datos())
nuevo_empleado = Empleado()
nuevo_empleado.sueldo()
