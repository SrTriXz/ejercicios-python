def sumatoria_recursiva(num):
    if num == 1:
        return 1
    return num + sumatoria_recursiva(num - 1)



while True:
    usuario = int(input("INGRESE UN NUMERO PORFAVOR ----->"))
    print(sumatoria_recursiva(usuario))


    

