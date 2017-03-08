from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# x in units of a, y in units of b, temp. T in units of q'''a^2/k.

fig = figure()
ax = Axes3D(fig)             # create 3D axes
x = np.arange(-1, 1.01, 0.1)
y = np.arange(-1, 1.01, 0.1)
x, y = np.meshgrid(x, y)
z = 0.5 * np.cos(np.pi*x/2) * np.cos(np.pi*y/2)
ax.plot_surface(x, y, z, rstride=2, cstride=4, cmap=cm.hot)
xlabel('x')
ylabel('y')
title('exact temperature solution')

show()

CS = contour(x, y, z)
clabel(CS, inline=0, fontsize=12)
title('exact temperature solution')
xlabel('x')
ylabel('y')
show()

# PS: import * is not recommended. (cf import of numpy as np included in the background, confusing). I left it because it works.
