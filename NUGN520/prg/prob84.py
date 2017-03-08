'''
   (explicit) iterative solution for cruciform unsteady heat conduction example
'''   

# initialize temp. values
t11, t21, t31, t41, t51 = 1000., 1000., 1000., 1000., 1000.
dx = 0.125
deltax, k, qtriple = (dx/12)**2, 1.085, 1.5e7    # BG units
ts = 1000.
dtg2 = (0.5*deltax)*qtriple/(2*k)
fo=0.25
print('temperature solution (degrees F):')
# iterate:
for i in range(21):
    t11n = (1-4*fo)*t11+fo*(t21+3*ts) + 2*fo*dtg2
    t21n = (1-4*fo)*t21+fo*(t31+t11+2*ts) + 2*fo*dtg2
    t31n = (1-4*fo)*t31+fo*(t41+t21+2*ts) + 2*fo*dtg2
    t41n = (1-4*fo)*t41+fo*(t51+t31+2*ts) + 2*fo*dtg2
    t51n = (1-4*fo)*t51+fo*(2*t41+2*ts) + 2*fo*dtg2
    # roll values
    t11, t21, t31, t41, t51 = t11n, t21n, t31n, t41n, t51n
    if i % 5 == 0:
        print('number of time steps: ', i+1)
        print(t11, t21, t31, t41, t51)
