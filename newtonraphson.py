def func(x):
    return x*x - x - 1

def derifunc(x):
    return 2*x - 1

def newtonraphson(x):
    h = func(x)/derifunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derifunc(x)
        x = x-h
    print("The value of the root is : ","%.4f"% x)

x = 1
newtonraphson(x)