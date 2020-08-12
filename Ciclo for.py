# Bucle for

for i in [1, 2, 3, 4, 5]:
    print("Hola mundo")
print("\n")

for i in [2, 10, 3, 4, "Demian"]: #Toma cualquier tipo de valor como 1 elemento mas
    print(f"Elemento: {i}")
print("\n")

coleccion = [2, 10, 3, 4, "Demian"] #Tambien podemos usar una variable
for i in coleccion:
    print(f"Elemento: {i}")
print("\n")

'''La colección también puede ser: CONJUNTO(SET) ···> { }    LISTA(LIST) ···> [ ]   TUPLA(TUPLE) ···> ( )'''

# creamos un diccionario de ejemplo

coleccion = {"Demian": 22, "Maria": 23, "Jose": 45, "Luis": 12}

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")
print("\n")

# la forma mas usada

coleccion = {"Demian": 22, "Maria": 23, "Jose": 45, "Luis": 12}

for clave, valor in coleccion.items(): #se usa la bibliotec "items"
    print(f"{clave} -> {valor}")
print("\n")

# tambien se pueden recorrer cadenas

coleccion = "Demian"

for i in coleccion:
    print(f"hola")  # La cantidad de veces que se imprime depende de la cantidad de caracteres que contenga la cadena
print("\n")
for i in coleccion:
    print(f"{i}")  # Se imprimen los caracteres de la cadena, caracter por caracter
print("\n")
for i in coleccion:
    print(f"{i}", end="")  # Para no listar los caracteres de la cadena.
print("\n")
for i in coleccion:
    print(f"{i}", end=".")  # Para separar los caracteres con por ejemplo, puntos.
