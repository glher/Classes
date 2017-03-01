'''
   symmetric cruciform 2D heat conduction illustration
'''

import numpy as np

m = 6    # size of system is m x m

print 'number of equations: ', m
# deltax, k, qtriple = (0.2/12)**2, 19.84, 1.e7    # BG units
# deltatg = 0.5*deltax**2*qtriple/k

amat = np.zeros((m,m))
b = np.zeros(m)
for i in range(m):          # i goes from 0 to m-1 here
    amat[i,i]= -1.0
    b[i] = -335.
for i in range(m-1):
    amat[i,i+1] = 0.25
    amat[i+1,i] = 0.25
amat[0,0] = 1.0     
amat[0,1] = -1.0    
b[0] = 35.
b[m-1] = -485.

print 'b vector', b
print 'system matrix:'
print amat

ysol = np.linalg.solve(amat,b)

print 
print 'temperature solution:'       
print ysol

# check of solution: 
print (np.dot(amat, ysol) - b <= 1.0e-12).all()

    
