"""
Illustrate simple contour plotting
"""

from pylab import *

# x in units of a, y in units of b, temp. T in units of q'''a^2/k.

def temp(x,y,max):
    term1 = 0.5*(1.-x*x)
    sum=0.0
    for i in range(max):
        sum += (-1)**i*np.cosh(lamb(i)*y)*np.cos(lamb(i)*x)/(
                   np.cosh(lamb(i))*lamb(i)**3)                                                                  
    return term1 -2.0*sum
    
def lamb(n):
    return (n+.5)*np.pi           # or use float(n)

def approx(x,y):
    return 0.75*0.5*(1.-x*x)*(1.-y*y)

delta = 0.025
x = np.arange(-1.0, 1.0, delta)
y = np.arange(-1.0, 1.0, delta)
X, Y = np.meshgrid(x, y)
Z = temp(X,Y,200)
#Z = approx(X,Y)

figure()
CS = contour(X, Y, Z)     # e.g., add ,20 to increase the number of contours
clabel(CS, inline=0, fontsize=12)
title('exact temperature solution')
xlabel('x')
ylabel('y')
show()


