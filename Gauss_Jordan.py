import numpy as np
import sys

def printMatrix(a,n):
    for i in range(n):
        for j in range(n+1):
            print(a[i][j],end='\t')
        print('\n')

n = int(input('Enter the umber of unknowns : '))
a = np.zeros((n,n+1))
x = np.zeros(n)

print('Enter the coefficients of the augmented matrix:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input('a['+str(i)+']['+str(j)+'] = '))
        
# Gauss Jordan method
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio*a[i][k]
    print('Iteration %d :'%i)
    printMatrix(a,n)

# Solution                
for i in range(n):
    x[i] = a[i][n]/a[i][i]
    
print('Solution : ')
for i in range(n):
    print('x%d = %0.2f'%(i,x[i]),end='\t')
    
'''
x + y + z = 9
2x -3y +4z = 13
3x + 4y + 5z = 40
soln: x = 1.0; y = 3.0; z = 5.0
'''