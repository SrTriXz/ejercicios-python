#crear funa agenda pero con funciones
contactos = {}
def añadir(nombre, numero):
    contactos[nombre]=numero

    return (f"{nombre} se ha añadido correctamente")

def eliminar(nombre):
    del(contactos[nombre])
    
def lista():
    print(contactos)
    
while True:
    print("0: AÑADIR \n 1: ELIMINAR \n 2: LISTA DE CONTACTOS")
    funcion = int(input("ingrese que quiere hacer"))

    while funcion > 2:
        print("ingrese correctamente el nombre")
        if funcion <= 2:
            break 

    if funcion == 0:
        print("A QUIEN DESEAS AÑADIR")

        nom = input("nombre: ")
        num = int(input("numero: "))

        añadir(nom,num)

    elif funcion == 1:
        print("A QUIEN DESEAS ELIMINAR")
        nom = input("nombre: ")
        while True:
            if nom not in contactos:
                print(f"{nom} no se encuntra en la lista de contactos")
            
            else:
                break

            eliminar(nom)

    else:
        for nombre, numero in enumerate(contactos):
            print(nombre, numero)





        
