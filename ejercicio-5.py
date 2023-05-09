#mostrar que se pueden hacer 3 opciones
print ("""INGRESA * PARA SUMAR
INGRESA ** PARA RESTAR
INGRESA *** PARA MULTIPLICAR""")
#preguntarle al usuario 2 numeros
funcion = input("que deseas realizar")
numero_1 = int(input("ingrese el primer numero porfavor: "))
numero_2 = int(input("ingrese el segundo numero porfavor: "))

#suma entre ellos
if funcion == "*":
    suma = numero_1 + numero_2
    print("la suma entre los dos numeros es " ,suma)

elif funcion == "**":
    resta = numero_1 - numero_2
    print("la resta entre los dos numeros es", resta)

elif funcion == "***":
    multiplicacion = numero_1 * numero_2
    print("la multiplicacion entre los dos numeros es", multiplicacion)

else:
    print("la opcion es incorrecta")
 
#resta entre ellos (primero con el segundo)
#multiplicacion
#si ingresa otra cosa mostrar que la opcion es incorrecta