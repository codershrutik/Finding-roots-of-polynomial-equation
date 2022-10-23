import math

def f(x):
    return x * x - x - 1

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return x*x - 1

def fixedPoint(x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration- %d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
x0 = input('Enter Guess: ')
e = 0.00001
N = 20

# Converting x0 and e to float
x0 = float(x0)

fixedPoint(x0, e, N)