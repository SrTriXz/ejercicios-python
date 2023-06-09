def sumatorio(num) :
    i = num + 1
    num -= 1
    i += num
    print(num)
    if num > 0:
        print( f"El resultado final es{i}")
    else:
        print("Fin de la ejecucion")


while True:
    usuario = int(input("INGRESE UN NUMERO PORFAVOR ----->"))
    print(sumatorio(usuario))