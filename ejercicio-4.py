#crear una variable numeor que el usuario va a poner 

numero = int(input("ingrese un numero porfavor: "))

if numero > 0:
    for i in range(numero + 1):
        if i % 2 == 0:
            print(i , "es numero par")

        else:
            print(i , "es numero impar")

#mirar los numeros pares e impares que hay hasta ese numero
