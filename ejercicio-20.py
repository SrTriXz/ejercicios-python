def recortar(numero, minimo, maximo):
    if numero > minimo and numero > maximo:
        return (f"el numero mayor es {numero}") 
    elif minimo > numero and minimo > maximo:
        return (f"el numero mayor es {minimo}")
    else:
        return (f"el numero mayor es {maximo}")

a = int(input("ingrese un numero porfavor: "))
b = int(input("ingrese un numero porfavor: "))
c = int(input("ingrese un numero porfavor: "))

print(recortar(a,b,c))


