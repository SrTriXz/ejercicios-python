#Escribir un programa que reciba una cadena de caracteres y 
#devuelva un diccionario con cada palabra que contiene y su frecuencia. 
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una
#tupla con la palabra más repetida y su frecuencia.



def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = input("ingrese un texto para medir")
print(count_words(text))
print(most_repeated(count_words(text)))
        



