#crear una tupla

#imprimir el ultimo elemento
#el numero de elementos que contine la tupla 
#la posicion donde se encuentra el numero 123
#lista con los primeros 3 elementos de la lista
#El elemento que hay en la posición con índice 4 de la tupla.
#El número de veces que aparece el número 4 en la tupla.

mi_tupla = ("HOLA", "MUNDO", 123, 6, [1,2,3])

print("el ultimo elemento de la tupla es", mi_tupla[-1])
print("el numero de elemtos que contiene la tupla es ", len(mi_tupla))
print("el numero 123 esta en la posicion ", mi_tupla.index(123))
print("lista de los primeros 3 elemtos", list(mi_tupla[:2]))
print("el elemento de la posicion 4 es", print(mi_tupla[4]))
print("el numero de veces que aparece el 4 es", mi_tupla.count(4))
