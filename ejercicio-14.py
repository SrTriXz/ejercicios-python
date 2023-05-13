from tkinter import *
class Tecla():
    def __init__(self,render,valor):
        global flag
        self.valor = valor
        if self.valor != "DEL" and self.valor != "MAY":
            self.main = Button(render,text = self.valor,command =  self.anadir)
        elif valor == "DEL":
            self.main = Button(render,text = self.valor,command = delete)
        elif valor == "MAY":
            self.main = Button(render,text = self.valor,command = self.mayus)

    def anadir(self):
        global flag
        añadir = self.valor.upper() if flag else self.valor.lower()
        texto = escrito.get() + añadir
        escrito.set(texto)
    def mayus(self):
        global flag
        flag = not flag
        if flag:
            color = "Green"
        else:
            color = "Red"
        self.main.config(
            bg = color
        )
flag = True
def delete():
    texto = escrito.get()
    escrito.set(texto[:len(texto)  - 1])
ordenTeclas = ["1234567890","QWERTYUIOP","ASDFGHJKL>","ZXCVBNM,.-",["DEL","MAY"," "]]


##VENTANA##
main = Tk()
main.geometry("460x300")
main.resizable(False,False)
##RESULTADO##
escrito = StringVar()
resultado = Entry(main,textvariable = escrito)
resultado.config(
bg = "Grey",
fg = "Black",
font = ("Consolas", 20)
)
resultado.grid(
ipadx = 500,
column = 0,
row = 0,
columnspan = 12,
sticky = W
)
##FRAME TECLAS##
teclaF = Frame(main)
teclaF.config(
    bg = "DarkSlateGray"
)
teclaF.grid(
    ipadx = 501,
    ipady = 480,
    sticky = W,
    column = 0,
    row = 1
)
Bvotones = []
for fila,conjunto in enumerate(ordenTeclas):
    for columna,boton in enumerate(conjunto):
        X = 13
        columnspan = 1
        if boton == "DEL" or boton == "MAY":
            X = 7
            columnspan = 10
        elif boton == " ":
            X = 170
            columnspan = 10
        tecla = Tecla(teclaF,boton)
        color = "DarkSlateGrey"
        if boton == "MAY":
            color = "Green"
        tecla.main.config(
            bg = color,
            relief = "flat",
            justify = LEFT
        )
        tecla.main.grid(
            ipadx = X,
            ipady = 11,
            column = columna,
            columnspan = columnspan,
            row = fila,
            sticky = NW
        )
        Bvotones.append(tecla.main)




main.mainloop()









































































