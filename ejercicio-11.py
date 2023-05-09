#dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas
#pero no debe repetirse ningun elemento en la nueva lista


lista1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]

lista2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

lista3 = []

for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)
print (lista3)