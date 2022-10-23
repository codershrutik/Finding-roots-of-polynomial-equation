maxiter = 20

def func(x):
    return (x*x - x - 1)

def regulafalsi(a,b):
    if func(a)*func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c=a
    for i in range(maxiter):
        c = (a * func(b) - b * func(a))/(func(b) - func(a))

        if func(c) == 0:
            break
        elif func(c)*func(a)<0:
            b = c
        else:
            a = c
    print("The value of root is : " , '%.4f' %c)

a = 1
b = 2
regulafalsi(a,b)
