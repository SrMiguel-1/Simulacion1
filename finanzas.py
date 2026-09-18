def fib(numero):
    x,y= 0,1
    list=[]
    resultado=0
    resultado= resultado * x
    while x<=numero:
        list.append(x)
        print("Hello world..")
        x, y=y, x+y
    return list
    print("resultado de suceción de fubinacci: ", resultado)


fib(8)

