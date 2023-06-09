def sumatorio(num):
    numero = 0
    
    for i in range(num + 1):

        numero += i
        
    return numero 
  

while True:
    usuario = int(input("Ingrese un numero: "))
    print(sumatorio(usuario))






