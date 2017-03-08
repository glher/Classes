'''
   (explicit) iterative solution for cruciform unsteady heat conduction example
'''   

# initialize temp. values
t00, t01, t10, t11, t20, t21, t30, t31, t40, t41, t50, t51 = 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000.
delg2, ts = 35., 1000.
dx = 0.125
deltax, k, qtriple = (dx/5)**2, 19.84, 1.e7    # BG units
ts = 600.
dtg = (0.5*deltax)*qtriple/k
fo=0.
print('temperature solution (degrees F):')
# iterate:
for i in range(21):
    t11n = (1-4*fo)*t11+fo*(t21+3*ts) + 2*fo*delg2
    t21n = (1-4*fo)*t21+fo*(t31+t11+2*ts) + 2*fo*delg2
    t31n = (1-4*fo)*t31+fo*(t41+t21+2*ts) + 2*fo*delg2
    t41n = (1-4*fo)*t41+fo*(t51+t31+2*ts) + 2*fo*delg2
    t51n = (1-4*fo)*t51+fo*(2*t41+2*ts) + 2*fo*delg2
    # roll values
    t11, t21, t31, t41, t51 = t11n, t21n, t31n, t41n, t51n
    if i % 5 == 0:
        print('number of time steps: ', i+1)
        print(t11, t21, t31, t41, t51)
