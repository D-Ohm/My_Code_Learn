# Bucle While

# El bucle while se puede ejec utar n veces, puediendo ser n = a infinito.

import math  # importa el modulo SQRT para sacar raices cuadradas

numero = float(input("Digite un numero: "))

while numero < 0:
    print("Error -> deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


#otro ejemplo

i = 0

while i<10:
    print("Hola mundo")
    i += 1

#otro ejmplo

i = 1

while i<=10:
    print(i)
    i += 1
