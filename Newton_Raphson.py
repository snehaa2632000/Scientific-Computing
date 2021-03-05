import numpy as np
from sympy import * 

x = symbols('x')
#inp = input('Enter the exp :')
expr = 2 * x**3 - 2 * x - 5
print("Given expression : {}".format(expr))

expr_diff = expr.diff(x)
print("Derivative of expression with respect to x : {}".format(expr_diff.doit())) 

f = lambdify(x,expr,'numpy')
f_diff = lambdify(x,expr_diff,'numpy')

def func(x):
    return f(x)

def derivative(x):
    return f_diff(x)

def newtonRaphson(x): 
    itr = 1
    h = func(x) / derivative(x) 
    while abs(h) >= 0.000001: 
        h = func(x)/derivative(x) 
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h
        
        print('Iteration-%d => x = %0.6f'%(itr,x))   
        itr = itr + 1
        
    print("The value of the root is : ", "%.4f"% x) 

#Initial value
for i in range(10):
    m = func(i)
    i = i+1
    n = func(i)
    if m <= 0 and n>=0:
        a = i - 1 
        b = i
        break
    
x_0 = (a+b)/2
print(x_0)

newtonRaphson(x_0)  
