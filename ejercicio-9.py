#realizar un programa que le pida a el usuario un numero 1-9
#si el numero esta en la lista, notificarlo
#sino, repetir el proceso hasta que acierte un numero

numeros = [1,3,6,9]

while True:
    usuario = int(input("ingrese un numero porfavor 1-9: "))
    if usuario > 0 and usuario < 10:
        if usuario in numeros:
            print("acertaste un numero de la lista")
            break

        else:
            print("el numero no esta en la lista")
