# Diccioniarios 1a
# Los diccionarios son desoradenados y requieren de dos elementos clave y valor 'clave:valor'

diccionario = {"azul":"blue", "rojo":"red","verde":"green"}

diccionario["amarillo"] = "yellow" #para agregar un nuevo elemento al diccionario
del(diccionario["verde"]) # Al eliminar la clave tambien se elimina el valor

print(diccionario)


#Diccionario clase 1b

diccionario = {"Demian":{"edad": 36,"estatura": 1.73},"Alejandro":[22,1.73],"Jose":[21, 1.75],"Maria":[22, 1.67]}

print(diccionario)

print(diccionario["Demian"])

print(diccionario["Maria"])

# Diccionarios clase 2

equipo = {10:"Paulo Dybala", 11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Mandzukic"}

print(equipo.get(10,"no existe un jugador en esa posición"))

print(equipo.get(9,"no existe un jugador en esa posición")) #con metodo "get" evito que salga error de excepcion

print( 12 in equipo)

print(11 in equipo) # arroja un True o un False ya que confirma si la clave esta en el diccionario, sirve para buscar dentro de un diccionario

print(equipo.keys()) # sirve para mostrar solo las claves del diccionario

print(equipo.values()) # sirve para mostrar solo los valores

print(equipo.items()) # sirve para mostrar los valores y las claves, pero a diferencia de poner solo el nombre del diccionario se usa mas para recorrer diccionarios con el bucle "for", lo coloca dentro de una tupla.

print(len(equipo)) #para saber cuantos elementos tiene el diccionario

equipo.clear() # borra todos los elementos del diccionario

print(equipo)