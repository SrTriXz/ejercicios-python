class Persona():
    def __init__(self, nombre, apellido, edad, id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.id = id
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

emita = Persona("Emmanuel", "Torres", 17, "1018197654")
emita.presentarse()
