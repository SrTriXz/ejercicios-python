class Galleta:
    chocolate = False
    def __init__(self) -> None:
        print("Se acaba de crear una galleta")
    def chocolatear(self):
        self.chocolate = False
        print("la galleta se acaba de chocolatear")
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocomalteada")
        else:
            print("No soy una galleta chocomalteada")
                


g = Galleta()
g.chocolatear()
g.chocolate
g.tiene_chocolate()

