import numpy as np
from sympy import * 

x = symbols('x')
expr = 1 * x**3 - 5 * x**2 + 7 * x - 3
print("Given expression : {}".format(expr))

expr_diff = expr.diff(x)
print("Derivative of expression with respect to x : {}".format(expr_diff.doit())) 

expr_ddiff = expr_diff.diff(x)
print("Double Derivative of expression with respect to x : {}".format(expr_ddiff.doit())) 

f = lambdify(x,expr,'numpy')
f_diff = lambdify(x,expr_diff,'numpy')
f_ddiff = lambdify(x,expr_ddiff,'numpy')

def func(x):
    return f(x)

def derivative(x):
    return f_diff(x)

def double_derivative(x):
    return f_ddiff(x)

def newtonRaphson(x): 
    itr = 1
    h = (func(x) * derivative(x))/(derivative(x)**2 - (func(x)*double_derivative(x)))
    while abs(h) >= 0.0001: 
        h = func(x)/derivative(x) 
        # x(i+1) = x(i) - f(x) * f'(x) / (f'(x))^2 - f(x)*f''(x) 
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
print(a,'  ',b)
print('x_0 = ',x_0)

newtonRaphson(x_0)  
