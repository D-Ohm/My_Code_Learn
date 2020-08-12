num1=10
num2=5
resultado = num1 + num2
print(resultado)
'''tambien sirve con restav"-", multiplicacion "*", division "/"'''
'''para pobtener resultados de divisiones con un numero entero en lugar de un decimal se usa el sgte simbolo "//"'''
resultado = 10 /3
print(resultado)

#nos da un valor decimal como resultado
resultado = 10//3
print(resultado)
#nos da un numero entero como resultado, simpre redondeando hacia abajo
'''Para hallar el modulo de una division se usa "%"'''
num1= 5
num2= 2
resultado = num1 % num2
print(resultado)
#para elevar un numero a una determinada potencia se usa el op "**"
num1= 2
num2= 5
resultado = num1 ** num2
print(resultado)

'''prioridad de los operadores, lo primero que se evalua son los parentesis,
luego los de exponenciacion, luego los de multiplicacion, division, modulo y por ultimo la suma y resta,'''

resultado = 3**3*(13/5 -(2*4))
print(resultado)

'''primero resuelve los parentesis mas internos, de adentro hacia afuera, luego la division dentro del parentesis,
luego la resta dentro del parentesis, luego la potencia y por ultimo la multiplicacion'''
