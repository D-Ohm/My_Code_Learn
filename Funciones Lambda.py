#Funciones lambda, solo ejecutan 1 linea  de codigo (1 solo statement)

x = lambda a : a + 10
print(x(10))
print(x(11))

#puede tener cualquier cantidad de parametros
y = lambda a,b : a * b
print(y(4, 5))

z = lambda a, b, c: a + b + c
print(z(2, 3, 7))