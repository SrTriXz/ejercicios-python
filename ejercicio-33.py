class Galleta:
    chocolate = False

    def __init__(self):
        self.chocolate = True 

    def tiene_chocolate():
        if self.chocolate:
            print("SOY UNA GALLETA RELLENA DE CHOCOLATE :(")
        else:
            print("NO SOY UNA GALLETA RELLENA DE CHOCOLATE :)")


g = Galleta()
print(g.chocolate)
print(g.tiene_chocolate())
