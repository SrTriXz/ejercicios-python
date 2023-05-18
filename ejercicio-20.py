def recortar(numero, minimo, maximo):
    if numero > minimo and numero > maximo:
        print(f"{numero} es el numero mayor")
    elif minimo > numero and minimo > maximo:
        print(f"{minimo}es el numero mayor") 
    else:
        print(f"{maximo} es el numero mayor")

a = int(input("ingrese un numero porfavor: "))
b = int(input("ingrese un numero porfavor: "))
c = int(input("ingrese un numero porfavor: "))

print(recortar(a,b,c))