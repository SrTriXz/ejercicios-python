agenda = {}

llave = input("QUE DESEAS AGREGAR: ")
palabra = int(input("NUMERO QUE DESEAS AGREGAR: "))

agenda[llave] = palabra
print(agenda)
otro = int(input("NUMERO QUE DESEAS AGREGAR: "))
agenda[llave] = otro

print(agenda)