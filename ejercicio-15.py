conjunto = {"Maria", "Marta", "Camilo", "Juan", "Marcos", "Elvira"}

administadores = {"Juan", "Marta"}

administadores.discard("Juan")
administadores.add("Marcos")


for i in conjunto:
    if i not in administadores:
        print(i , "no es administrador")
    else:
        print(i ,"es administrador")
    
