def agregar(lista,elemento):
    try:
        if elemento  not in lista:

            lista.append(elemento)
        else:
            raise ValueError
        
    except ValueError:
        print("no se puede añadir numeros repetidos", elemento)


elementos= [1,2,3,4]
print(agregar(elementos, 4))
print(agregar(elementos, 2))
print(agregar(elementos, 5))
print(elementos)

