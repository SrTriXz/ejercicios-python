class pelicula:
    peliculas = []
    def __init__(self, titulo,lanzamiento,duracion) -> None:
        self.lanzamiento = lanzamiento
        self.titulo = titulo
        self.duracion = duracion
        print(f"se ha creado la pelicula {self.titulo}")
    
    def __del__(self):
        print(f"se ha borrado la pelicula {self.titulo}")

    def __str__(self):
        return self.titulo, self.lanzamiento, self.duracion 
    
    def __len__(self):
        print(f"la pelicula dura {self.duracion}")
    

pelicula("Padrino", "1978", "175 minutos")
str(pelicula)

