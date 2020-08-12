# Funciones III

# Creamos una funcion que devuelva el factorial de un numero

def factorial(num):
    resultado = num
    for i in range(num - 1, 1, -1):
        resultado = resultado * i

    return resultado


print(factorial(5))  # debe dar 120


# Creamos una funcion que arroje los numeros que hay en orden sucesivo entre un numero y otro.

def numerosEntre(n1, n2):
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux
    for i in range(n1 + 1, n2):  # 'n1+1' para arranque en siguiente número al primero
        print(i)


numerosEntre(10, 1)
