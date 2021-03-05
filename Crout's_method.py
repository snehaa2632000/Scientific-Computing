import numpy as np

def crout(A,n):

    L = np.zeros((n,n))
    U = np.zeros((n,n))

    for k in range(n):
        U[k,k] = 1 

        for j in range(k,n):
            sum_0 = sum([L[j,s] * U[s,k] for s in range(j)]) #range from index 0
            #reversed index
            L[j,k] = A[j,k] - sum_0 

        for j in range(k,n):
            sum_1 = sum([L[k,s] * U[s,j] for s in range(j)]) #range from index 0
            U[k,j] = (A[k,j] - sum_1)/L[k,k]

        print('Itr ',k+1,' :- L =',L)
        print('\n U = ',U)
    return L,U


n = int(input('Enter the order of the matrix : '))
a = np.zeros((n,n))
#a = np.array([[60.0, 30.0, 20.0], [30.0, 20.0, 15.0], [20.0, 15.0, 12.0]])

print('Enter the matrix coefficients: ')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('a['+str(i)+']['+ str(j)+']='))

l,u = crout(a,n)