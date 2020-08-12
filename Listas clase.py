# listas

smartphones = ["Xiomi", "Iphone", "Huawei", "Samsung"]

print(smartphones[-1])
'''Si coloco un numero negativo llamo elementos de la lista del ultimo 
al primero, comenzando siempre por el -1, y si el numero es positivo, llamo del primero al ultimo, comenzando siempre
desde cero'''

del smartphones[0]
# Para borrar elementos de una lista, con metodo 'del'

print(smartphones)

smartphones.remove("Huawei")
smartphones.remove("Samsung")
# Eliminar elementos con metodo 'remove': se pueden eliminar mas elementos, repitiendo abajo el codigo con otro nombre

print(smartphones)

smartphones.append("Samsung")
smartphones.append("Xiomi")
smartphones.append("Huawei")

print(smartphones)
# 'Append' se parece a remove pero sirve para añadir nuevos elementos a la lista, añade al final de la lista!!

smartphones.insert(1, "Motorola")
smartphones.insert(-1, "Nokia")
smartphones.insert(2, "Sony")

print(smartphones)
