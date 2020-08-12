# Ejercicio de contraseña (enviada)

pssw = "nueva"
ingreso = input('Ingrese contraseña: ')

if ingreso != pssw:
    print("Contraseña incorrecta, puede intentar 2 veces mas")
    ingreso = input('Ingrese contraseña: ')
    if ingreso != pssw:
        print("Contraseña incorrecta, puede intentar 1 vez mas")
        ingreso = input('Ingrese contraseña: ')
        if ingreso != pssw:
            print("Contraseña incorrecta, cantidad de intentos agotados, contacte a su administrador.")
        else:
            print("Contraseña correcta, bienvenido!")
    else:
        print("Contraseña correcta, bienvenido!")
else:
    print("Contraseña correcta, bienvenido!")
