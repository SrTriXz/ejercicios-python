def par_o_impar(numero):
    for i in range(numero):
        if i % 2 == 0:
            print(f"{i} es un numero par") 
        else:
            print(f"{i} el numero es impar")

arberto_instantaneo = int(input("ingrese un numero porfavor: "))
print(par_o_impar(arberto_instantaneo + 1))

