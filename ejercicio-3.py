matriz = [
    [8,  7,  0],  
    [34, 2, -1],
    [5, -5, 12]
]

for i, fila in enumerate(matriz):
    for j,columna in enumerate (fila):
        matriz[i][j] = columna % 2
    print(fila)





# $ git remote set-url origin <url> | para cambiar la url actual ok ok gracias
while True:
    print("Chao")