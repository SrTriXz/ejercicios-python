def recortar(numero,minimo,maximo):
    if numero < minimo:
        return minimo
    elif numero>maximo:
        return maximo
    
    return numero



print(recortar(5,0,3))