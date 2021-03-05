import numpy as np

n = int(input('Enter order of matrix: '))
a = np.zeros((n,2*n))

# Reading matrix coefficients
print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
        
# Augmenting Identity Matrix of Order n
for i in range(n):        
    for j in range(n):
        if i == j:
            a[i][j+n] = 1
            
#Applying Gauss Jordan elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(2*n):
                a[j][k] = a[j][k] - ratio * a[i][k]
    
    print('\nItr',i+1,' : ')
    for x in range(n):
        for y in range(n, 2*n):
            print(a[x][y], end='\t')
        print()

# Row operation to make principal diagonal element to 1
for i in range(n):
    tmp = a[i][i]
    for j in range(2*n):
        a[i][j] = a[i][j]/tmp

# Displaying Inverse Matrix
print('\nInverse Matrix:')
for i in range(n):
    for j in range(n, 2*n):
        print(a[i][j], end='\t')
    print()