x =10

def myFun():
    global x
    x = 20
    print("Inside Function",x)

myFun()

def myFun2():
    res = x +2
    print("Inside Function",res)

myFun2()