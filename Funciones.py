# Funciones

def my_function():
    print('Hello World')


my_function()


# otra forma
def my_function2(name):
    print('Hello ' + name + '!')


my_function2('Demian')


# Con argumento por defecto
def my_function3(age, name='Demian'):
    print('Hello ' + name + ', your age is ' + str(age) + '!')


my_function3(37, )


# Cambiando el argumento por defecto
def my_function3(age, name='Demian'):
    print('Hello ' + name + ', your age is ' + str(age) + '!')


my_function3(37, 'men')


# tambien puede ser

def sum_numbers(a, b):
    return a + b


suma = sum_numbers(29, 1)
print(suma)

print('\n')
# La funcion se llama a si misma de forma recursiva

def recursion(k):
    if k > 0:
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


recursion(7)
