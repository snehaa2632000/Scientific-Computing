import numpy as np

def printMatrix(a,n):
    for i in range(n):
        for j in range(n):
            print(a[i][j],end='\t')
        print('\n')

def gauss_jacobi(a,b,itr=20,x=None):
    if x is None:
        x = np.zeros(len(a[0]))
        
    diagonal_matrix = np.diag(a)
    r = a - np.diagflat(diagonal_matrix)
    
    x_prev = np.zeros(n)
    
    for i in range(itr):
        print('Itr',i,' : ')
        x = (b-np.dot(r,x))/diagonal_matrix
        print(x,end='\n')
        
        if np.allclose(x_prev,x):
            break
        x_prev = x
        
    return x

n = int(input('Enter the number of unknowns : '))
a = np.zeros((n,n))
b = np.zeros(n)
x = np.zeros(n)
guess = np.ones(n)

print('Enter the coefficients of the equations:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('a['+str(i)+']['+str(j)+'] = '))
        
    b[i] = float(input('b['+str(i)+'] = '))
        
print('The given coefficients matrix :\n')
printMatrix(a,n)
print('The given \'b\' matrix :\n',b)
        
x = gauss_jacobi(a,b,20,guess)

print('\n\n The final solution matrix :\n',x)