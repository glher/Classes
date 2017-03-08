from pylab import *
from mpl_toolkits.mplot3d import Axes3D

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

fig = figure()
ax = Axes3D(fig)             # create 3D axes
X = np.arange(-1, 1, 0.5)
Y = np.arange(-1, 1, 0.5)
X, Y = np.meshgrid(X, Y)
Z = temp(X,Y,200)
print(X)
print(Y)
print(Z)
ax.plot_surface(X, Y, Z, rstride=2, cstride=4, cmap=cm.hot)
xlabel('x')
ylabel('y')
title('exact temperature solution')

# savefig('../figures/plot3d_ex.png',dpi=48)
show()


