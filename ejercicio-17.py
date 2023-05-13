tareas = [[6, "distribucion"],
          [2, "diseño"],
          [1, "concepcion"],
          [7, "mantenimiento"],
          [4, "produccion"],
          [3, "planificacion"],
          [5, "pruebas"]
          ]

print ("----TAREAS DESORDENADAS----")
for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque

cola = deque()
tareas.sort()


for tarea in tareas:
    cola.append(tarea[1])
print(cola)


