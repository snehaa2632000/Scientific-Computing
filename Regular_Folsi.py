import numpy as np
from sympy import * 

x = symbols('x')
inp = input("Enter the function : ")
expr = simplify(inp)
#expr = x**3 + 3 * x - 5
print("Given expression : {}".format(expr))

f = lambdify(x,expr,'numpy')

def func(x):
    return f(x)

def regularFolsi(x0,x1):
    e = 0.00001
    itr = 1
    flag = True
    while flag:
        x2 = (x0*func(x1) - x1*func(x0))/(func(x1)-func(x0))
        print('Iteration - %d, x2 = %0.4f and f(x2) = %0.6f'%(itr,x2,func(x2)))
         
        if func(x0)*func(x2)<0:
            x1 = x2
        else:
            x0 = x2
        itr = itr+1
        flag = abs(func(x2))>e
    print('Root = %0.6f'%x2)
        

#Initial value
for i in range(10):
    m = func(i)
    i = i+1
    n = func(i)
    if m * n < 0:
        a = i - 1 
        b = i
        break
    
print('Value of x0 = %d  x1 = %d'%(a,b))    
regularFolsi(a,b)  