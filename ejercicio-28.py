
def separar(a):
    for i in a:
        if i %2 == 0:
            pares.append(i)

        else:
            impares.append(i)

    return pares, impares

    


pares=[]
impares=[]
lista=[]


while True:
    eleccion = int(input("ingrese una lista porfavor: "))
    if eleccion == 000:
        print(separar(lista))
        break 
    lista.append(eleccion)
    print(lista)