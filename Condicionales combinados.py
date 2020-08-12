# Condicionales combinados

edad = int(input("Digite su edad: "))

if 0<edad<110:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Edad incorrecta")
'''El prmer 'if' dice (0<edad<100) que es equivalente a decir (edad>0 and edad<100)'''