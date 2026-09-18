def fib(numero):
    x,y= 0,1
    list=[]
    while x<=numero:
        list.append(x)
        print("Hello world")
        x, y=y, x+y
    return list
fib(8)
