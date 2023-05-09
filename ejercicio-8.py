#realiza un programa donde el usuaario digite la cantidad de numeros que va a introducir
#realizar la media entre los numeros que introdujo


print("aplicacion para saber la media")

repeticiones = int(input("ingrese la cantidad de numeros que va a introducir: "))
suma = 0 
for i in range(repeticiones):
    suma += (float(input("ingrese un numero")))
    
print("la media de los numeros es ", suma/repeticiones)