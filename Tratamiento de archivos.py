# Archivos de texto, abrir, cerrar y leer archivos

archivo_estudiantes = open("estudiantes.txt", "w")  # Abrimos archivo
# 'w' Crea archivo para escritura, 'w+' para lectoescritura, si ya existia, borra y crea uno nuevo con nuevo contenido
# 'a' Para agregar contenido al final de la ultima linea solo para escritura, 'a+' para lectoecritura
# 'w+' borra todo y sobreescribe el archivo

for est in ("Karen\n", "Demian\n", "Nieve\n"):  # El contenido
    archivo_estudiantes.write(est)  # Lo escribo en el archivo creado 'archivo_estudiantes'

archivo_estudiantes.close()  # Cerramos Archivo

archivo_estudiantes = open("estudiantes.txt", "r")  # 'r' para leer, 'r+' es para lectoecritura
# Con 'r+' sobreescribe los primeros caractreres del texto
print(archivo_estudiantes.readable())  # Devuelve True si es legible
print(archivo_estudiantes.read())  # Lee el archivo completo
archivo_estudiantes.close()

archivo_estudiantes = open("estudiantes.txt", "r")
print(archivo_estudiantes.readline())  # Lee linea por linea
print(archivo_estudiantes.readline())
archivo_estudiantes.close()

archivo_estudiantes = open("estudiantes.txt", "r")
print(archivo_estudiantes.readlines())  # Lee el archivo completo en un array
print(archivo_estudiantes.readlines())  # No lo vuelve a leer porque ya esta hecho, no lo relee 2 veces
archivo_estudiantes.close()

archivo_estudiantes = open("estudiantes.txt", "r")  # Debo volver a abrirlo para que lo vuelva a leer
print(archivo_estudiantes.readlines()[1])  # Con [1] lee el primer elemento del array, con [2] el segundo y así...
archivo_estudiantes.close()

archivo_estudiantes = open("estudiantes.txt", "r")
for estu in archivo_estudiantes:  # Recorremos el array para extraer linea por linea
    print(estu)
print(archivo_estudiantes.readlines())  # Devuelve array vacio [] porque el for ya extrajo el todo contenido del array
archivo_estudiantes.close()

# Eliminar archivos
import os

# importamos libreria 'os'

archivo = (str(input("\nIngrese el nombre del archivo a crar: ")))

nuevo_archivo = open(f'{archivo}', "w")  # Creamos un nuevo archivo
nuevo_archivo.writelines(["\nNueva linea\n", "segunda linea"])  # creamos el contenido
nuevo_archivo.close()

nuevo_archivo = open(f'{archivo}', "r")  # Lo leemos para comprobar que esta todo ok
print(f"\nEl archivo {archivo} es legible ahora: ", nuevo_archivo.readable())
print(f"\nCual es el contendido del archivo {archivo}?", nuevo_archivo.read())
nuevo_archivo.close()

nuevo_archivo2 = ""
nuevo_archivo3 = ""

archivo2 = (str(input("\nIngrese el nombre del archivo a borrar: ")))

try:
    os.remove(f'{archivo2}')
except FileNotFoundError:
    print(f"\nNo existe el archivo {archivo2}")
else:
    print(f"\nEl archivo {archivo2} fue borrado exitosamente")

try:
    nuevo_archivo2 = open(f'{archivo2}', "r")
    nuevo_archivo2.close()
except FileNotFoundError:
    print(f"\nIntentando abrirlo encontramos que el archivo {archivo2} fue borrado o no existe el archivo")

try:
    nuevo_archivo3 = open(f'{archivo}', "r")
except FileNotFoundError:
    print(f"\nIntentando abrirlo encontramos que el archivo {archivo} fue borrado o no existe el archivo")
else:
    print(f"\n El archivo {archivo} es legible ahora? ", nuevo_archivo3.readable())