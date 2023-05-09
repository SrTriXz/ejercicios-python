

while True:
    numero_entero = int(input("introduzca un numero entero 1-9: "))

    if numero_entero >= 1 and numero_entero <= 9:
        for multiplo in range(1,101):
            if multiplo % numero_entero == 0:
                print(multiplo) 


