
from colorama import Back, Fore, init           #funcion para poner colores

listaPendientes = {             
    "LUNES":[] , 
    "MARTES": [],
    "MIERCOLES": [],
    "JUEVES": [],
    "VIERNES": []
}
    


def añadir():
    pendiente = input("¿Qué deseas agregar?\n=> ")
    while True:
        dia = input("¿Pa qué dia de la semana?\n=> ").upper()

        if not (dia in listaPendientes.keys()):
            print("El día que has digitado no existe.\n\n")
        else:
            break

    listaPendientes[dia].append(pendiente)

def mostrarDia(dia):
    print(f"{Fore.BLACK}{Back.LIGHTGREEN_EX}====={dia}====={Fore.RESET}{Back.RESET}")
    dia = listaPendientes[dia]
    for i, pendiente in enumerate(dia):
        print(f"\t{i + 1}) {pendiente}")
    if len(dia) == 0:
        print("\tNo hay tareas aún...")

def eliminar():
    dia = input("¿A que dia quieres acceder?\n").upper()
    mostrarDia(dia)

    if not (dia in listaPendientes.keys()):
        print("El día que has digitado no existe.\n\n")
        return eliminar()
    dia = listaPendientes[dia]
    numPendiente = int(input("¿Que número pendiente deseas eliminar?\n=> "))

    if numPendiente >= len(dia):
        print("El índice no es acorde a los elementos.\n\n")
        return eliminar()

    eliminado = dia.pop(numPendiente)
    
    print(f"La tarea '{eliminado}' ha sido eliminada con éxito")

def listar():
    dias = listaPendientes.keys()
    for dia in dias:
        mostrarDia(dia)
       

def chao():
    print(f"{Fore.YELLOW}Hasta pronto!!")
    exit()

init()



msg = \
f"""
{Fore.GREEN}0) AÑADIR
{Fore.RED}1) ELIMINAR
{Fore.BLUE}2) MOSTRAR LISTA DE PENDIENTES
{Fore.MAGENTA}3) SALIR DE LA AGENDA
{Fore.RESET}{Back.RESET}
"""
print(f"{Back.RED}{Fore.BLACK}-----BIENVENIDOS A TU AGENDA PERSONAL-----{Fore.RESET}{Back.RESET}")

try:
    while True:
        print(msg)
        usuario = int(input("=> "))
        opciones = [añadir, eliminar, listar, chao]
        if usuario >= len(opciones):
            print(f"{Back.RED}{Fore.BLACK}No existe esa opción{Fore.RESET}{Back.RESET}\n\n")
            continue
        accion = opciones[usuario]
        accion()
except KeyboardInterrupt:
    chao()














#fin