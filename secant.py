def f(x):
    return pow(x, 2) - x - 1

def secant(x1, x2, e):
    i = 0
    xm1 = 0
    xm2 = 0
    check = 0
    if (f(x1) * f(x2) < 0):
        while (1):
            xm1 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
            check = f(x1) * f(xm1)
            if (check == 0):
                break

            x1 = x2
            x2 = xm1

            i = i + 1

            xm2 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
            if (abs(xm2 - xm1) < e):
                break

        return xm1
    else:
        return -1


print(secant(1, 2, 0.00001))