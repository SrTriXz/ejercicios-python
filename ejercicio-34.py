fiesta = ["carlos", "ramona", "maria", "kelly", "carnaldo", "crsitiano"]

# Función: devuelve nueva lista
def lista(estudiantes, num, nuevo):
    #Creamos una copia del array
    nuevosEstudiantes = [ estudiante for estudiante in estudiantes ]
    #Si num > 0 entonces returnar un array con el array quitando los elementos y añadir el nuevo al final
    
    # if num > 0:
    #     nuevosEstudiantes = nuevosEstudiantes[:-num]
    while num > 0:
        nuevosEstudiantes.pop()
        num -= 1
    #En todos los casos hay que añadir nuevo estudiantes
    nuevosEstudiantes.append(nuevo)
    return nuevosEstudiantes


print( lista(fiesta, 4, "karla") )






