#crear una agenda de contactos

contactos = {}

while True:
    print("""AÑADIR = 1
    ELIMINAR = 2
    LISTA DE CONTACTOS = 3
    SALIR = 4""")

    eleccion = int(input("Que deseas realizar: "))

    if eleccion == 1:
        nombre = input ("ingrese el nombre: ")
        numero = int(input("ingrese el numero: "))

        contactos[nombre] = numero

    elif eleccion == 2:
        print(list(contactos), "Lista de contactos")
        while True:
            eliminar = input("¿a quien deseas eliminar?")
            if eliminar in contactos:
                contactos.pop(eliminar)
                break
            else:
                print (eliminar, "no se encuentra en la lista de contactos")

    elif eleccion == 3:
        eleccion2 = input("mostrar la agenda con numeros")
        if eleccion2 == "si":
            print (contactos)
        elif eleccion2 == "no":
            print(list(contactos))

    elif eleccion == 4:
        break


    else:
        print("la opcion es incorrecta")



        



