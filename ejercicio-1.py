lista_palabras = [] #lista de palabras
while True:
    palabra = input("ingrese una palabra: ") #palabra del usuario #lista de palabras se incrementa en palabras
    lista_palabras.append(palabra)
    if palabra == "**":
        for indice, pal in enumerate(lista_palabras):
            print(indice + 1, pal[0])
        print("se acabo el programa")
        break

   
        

