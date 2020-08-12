#  Tratar con errores en Python
# try... except... else... finally...

try:
    num1 = int(input("Dividendo - Ingrese un numero entero: "))
    num2 = int(input("Divisor - Ingrese un numero entero:  "))
    print(num2 / num2)
except ZeroDivisionError as err:
    print(err)  # 'err' trae el mensaje de error de Python por defecto
except ValueError:
    print("Debe ingresar un numero entero")
else:
    print("No hubo error")

finally:
    print("Se ejecuta asi haya o no error")
