def super_funcion(*arg,**args):
    t = 0 
    for i in arg:
        t+=i
    print(f"sumatorio indetermiando es {t}")
    for e in args:
        print(e, " ", args[e])

super_funcion(-21212,232323,23232,34343,-4343,l= [1,2,3,4,5,6], n= 5)