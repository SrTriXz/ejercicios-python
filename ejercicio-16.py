caballero = {"Vida": 2, "Alcance": 2, "Defensa": 2, "Ataque": 2}
guerrero = {"Vida": 2, "Alcance": 2, "Defensa": 2, "Ataque": 2}
arquero = {"Vida": 2, "Alcance": 2, "Defensa": 2, "Ataque": 2}



caballero["vida"]= guerrero["Vida"]*2
caballero["Defensa"]= guerrero["Defensa"]*2

guerrero["Ataque"]= caballero["Ataque"]*2
guerrero["Alcance"]=caballero["Alcance"]*2

arquero["vida"]= guerrero["Vida"]
arquero["Defensa"]= guerrero["Defensa"]/2
arquero["Alcance"]= guerrero["Alcance"]*2


print("Arquer\t",arquero,"Guerrero\t",guerrero,"Caballero\t",caballero)
