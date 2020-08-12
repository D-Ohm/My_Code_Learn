# Ejercicio de contraseña (no enviada)

pssw: str = "nueva"
ingreso = input('Ingrese contraseña: ')
intentos = 1

while intentos < 3 and ingreso != pssw:
    intentos += 1
    print("Contraseña incorrecta")
    ingreso = input('Ingrese contraseña: ')
while intentos <= 3 and pssw == ingreso:
    intentos = 4
    print("Contraseña correcta, bienvenido!")
while intentos == 3 and ingreso != pssw:
    intentos = 4
    print("Contraseña incorrecta, cantidad de intentos agotados, contacte a su administrador.")
