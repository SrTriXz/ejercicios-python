def comversion_binary(num):
    while num >= 1:
        if num % 2 == 0:
            lista.append(0)
            
        else:
            lista.append(1)
            
        num/=2    
        
lista=[]

while True:
    try: 
        n = int(input("INGRESE UN NUMERO A COMVERTIR: "))

    except:
        print("DIGITE CORRECTAMENTE EL NUMERO")
        
    
    else:
        print(comversion_binary(n))
        print(str(lista[::-1]).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""))

        break