# Listas

lista = []
cantpal = 0
while cantpal == 0:
    while cantpal <= 4:
        palabras = str(input("Escriba una palabra : "))
        if palabras:
            lista.append(palabras)
            cantpal += 1
            print(lista)
        else:
            print("No hemos detectado niguna palabra")

    print('Lista de palabras completa...')

    while cantpal == 5:
        opcion = input('Si desea agregar una nueva palabra ingrese "1", si desea borrar alguna palabra ingrese "2", '
                       'si no ingrese "3": ')
        if opcion:
            if opcion == "1":
                paladd = str(input("¿Cuál palabra desea agregar?: "))
                lista.append(paladd)
                print(lista)
            elif opcion == "2":
                palrem = str(input("¿Cuál palabra desea borrar?: "))
                lista.remove(palrem)
                print(lista)
                if len(lista) == 0:
                    print("No hay palabras en la lista")
                    cantpal = 0
            elif opcion == "3":
                cantpal += 1
                print("Fin del programa, hasta luego.")
            else:
                print("Opción no válida")
        else:
            print("Elija una opción")