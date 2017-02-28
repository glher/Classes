import numpy as np

m = 23    # size of system is m x m

dx = 0.1
deltax, k, qtriple = (dx/12)**2, 19.84, 1.e7    # BG units
ts = 600.
dtg = (0.5*deltax)*qtriple/k

amat = np.zeros((m,m))
b = np.zeros(m)
    
amat[0,0] = 1.
amat[0,1] = -1.
b[0] = dtg/2.

amat[1,0] = -0.25
amat[1,1] = 1.
amat[1,2] = -0.5
amat[1,3] = -0.25
b[1] = dtg/2.


amat[2,1] = -0.5
amat[2,2] = 1.
amat[2,4] = -0.5
b[2] = dtg/2.

for i in range(3, m, 2):
    try:
        amat[i,i-2] = -0.25
        amat[i,i] = 1.
        amat[i,i+1] = -0.5
        amat[i,i+2] = -0.25
        b[i] = dtg/2.
    except IndexError:
        break

for i in range(4, m, 2):
    try:
        amat[i,i-2] = -0.25
        amat[i,i-1] = -0.25
        amat[i,i] = 1.
        amat[i,i+2] = -0.25
        b[i] = ts/4. + dtg/2.
    except IndexError:
        break

amat[m-1,m-1] = 1.
amat[m-1,m-2] = -0.25
amat[m-1,m-3] = -0.25
b[m-1] = ts/2. + dtg/2.


amat[m-2,m-2] = 1.
amat[m-2,m-1] = -0.5
amat[m-2,m-4] = -0.25
b[m-2] = ts/4. + dtg/2.

ysol = np.linalg.solve(amat,b)

print('Temperature solution:')

temp = []
for i in range(12):
    for j in range(2):
        if i == 0 and j == 1:
            continue
        temp.append("T(%s,%s)" % (i, j))
        
for i,t in enumerate(temp):
    print("%s = %.1f" % (t, ysol[i]))
    
# check of solution: 
if not np.allclose(np.dot(amat, ysol), b):
    print("Solution does not match!")
    

    
