# Calculadora
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = str(input(
    "Seleccione operación a realizar (digite '+' para sumar,'-' para restar,'*' para multiplicar,"
    "'/' para dividir): "))

if operacion == '+':
    suma = num1 + num2
    print(suma)
elif operacion == '-':
    resta = num1 - num2
    print(resta)
elif operacion == '*':
    multiplicacion = num1 * num2
    print(multiplicacion)
elif operacion == '/':
    division = num1 / num2
    print(division)
else:
    print("No es posible realizar la operación.")
