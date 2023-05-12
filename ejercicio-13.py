# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

while True:
    print("""* PARA AÑADIR
    ** PARA ELIMINAR
    *** PARA VER LOS CONTACTOS""")
    funcion = input("QUE DESEAS REALIZAR: ")

    if funcion == "*":
        contacto = input("ingrese el contacto")
        grupo.add (contacto)

    elif funcion == "**":
        eliminar = input("A QUIEN DESEAS ELIMINAR")
        if eliminar in grupo:
            grupo.remove(eliminar)
        else:
            print("el contacto no se encuentra en el grupo")
    elif funcion == "***":
        print(grupo)

    else:
        print("COMANDO INCORRECTO") 
         
