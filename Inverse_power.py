import numpy as np

n = int(input('Enter the order of the matrix : '))
a = np.zeros((n,n))
x = np.zeros((n))

print('Enter the matrix coefficients: ')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('a['+str(i)+']['+ str(j)+']='))
        
print('Enter the initial guess vector:')
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    
max_itr = int(input('Enter the maximum number of iterations:'))

# Power method
lambda_old = 1.0
condition = True
itr = 1

a_inv = np.linalg.inv(a)

while condition:
    x = np.matmul(a_inv,x)
    
    # fimding the new eigen value and vector
    lambda_new = max(abs(x))
    
    x = x/lambda_new
    
    print('Iteration ',itr,': Eigen value = %0.4f'%(lambda_new))
    print('Eigen vector: ')
    for i in range(n):
        print('%0.5f\t'%(x[i]))
        
    itr = itr+1
    #checking for maximum iterations
    if itr > max_itr:
        print('Not convergent in given maximum iteration.')
        break
    
    error = abs(lambda_new - lambda_old)
    print('Error='+ str(error))
    lambda_old = lambda_new
    condition = error > 0.001
    
print('\n\nFinal Eigen value = %0.4f'%(lambda_new))
print('Final Eigen vector: ')
for i in range(n):
    print('%0.5f\t'%(x[i]))
    