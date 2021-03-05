import numpy as np
import sys

def printMatrix(a,n):
    for i in range(n):
        for j in range(n+1):
            print(a[i][j],end='\t')
        print('\n')
        
def gaussSeidal(a,x,n):
    for i in range(n):
        d = a[i][n]
        for j in range(n):
            if j!=i:
                d = d - a[i][j]*x[j]
        x[i] = d/a[i][i]
    return x
        
n = int(input('Enter the number of unknowns : '))
a = np.zeros((n,n+1))
x = np.zeros(n)
temp = np.zeros(n) 

'''
4x + y + 2z = 4
3x + 5y + z = 7
x + y + 3z = 3
soln: x = 0.5; y = 1.0; z = 0.5
'''

print('Enter the coefficients of the augmented matrix:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input('a['+str(i)+']['+str(j)+'] = '))
        
for i in range(20):
    x = gaussSeidal(a,x,n)
    if np.allclose(x,temp):
        break
    temp = x.copy()
    print('Iteration ',i+1,': ',x)

print('Iteration ',i+1,': ',x)    
print('Solution: ',np.around(x,decimals = 4))