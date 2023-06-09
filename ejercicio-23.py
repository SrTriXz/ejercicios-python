def indeterminados(**diccionario):
    print(diccionario)
    for clave in diccionario:
        print(clave, " ", diccionario[clave])

indeterminados(
    saludo      = "Hola",
    pregunta    = "que pasa",
    numero      = 434,
    lista       = [1,2,3,4,"Hola"]
)

dicc = {
    "saludo"   : "Hola", # Clave : dict[clave]
    "pregunta" : "que pasa",
    "numero"   : 434,
    "lista"    : [1,2,3,4,"Hola"]
}






#Elefante en una nevera 