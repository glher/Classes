'''
   (explicit) iterative solution for cruciform unsteady heat conduction example
'''   

# initialize temp. values
t11, t21, t31, t41, t51, t61, t71, t81, t91, t101 = 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000.
t12, t22, t32, t42, t52, t62, t72, t82, t92, t102 = 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000.
dx = 0.125/2
deltax, k, qtriple = (dx/12)**2, 1.085, 1.5e7    # BG units
ts = 1000.
dtg2 = (0.5*deltax)*qtriple/(k)
fo=0.1
print('temperature solution (degrees F):')
# iterate:
for i in range(101):
    t11n = (1-4*fo)*t11+fo*(t21+2*ts+t12) + 2*fo*dtg2
    t21n = (1-4*fo)*t21+fo*(t31+t11+t22+ts) + 2*fo*dtg2
    t31n = (1-4*fo)*t31+fo*(t41+t21+t32+ts) + 2*fo*dtg2
    t41n = (1-4*fo)*t41+fo*(t51+t31+t42+ts) + 2*fo*dtg2
    t51n = (1-4*fo)*t51+fo*(t61+t41+t52+ts) + 2*fo*dtg2
    t61n = (1-4*fo)*t61+fo*(t71+t51+t62+ts) + 2*fo*dtg2
    t71n = (1-4*fo)*t71+fo*(t81+t61+t72+ts) + 2*fo*dtg2
    t81n = (1-4*fo)*t81+fo*(t91+t71+t82+ts) + 2*fo*dtg2
    t91n = (1-4*fo)*t91+fo*(t101+t81+t92+ts) + 2*fo*dtg2
    t101n = (1-4*fo)*t101+fo*(2*t91+ts+t102) + 2*fo*dtg2

    t12n = (1-4*fo)*t12+fo*(2*t11+ts+t22) + 2*fo*dtg2
    t22n = (1-4*fo)*t22+fo*(t12+t32+2*t21) + 2*fo*dtg2
    t32n = (1-4*fo)*t32+fo*(t22+t42+2*t31) + 2*fo*dtg2
    t42n = (1-4*fo)*t42+fo*(t32+t52+2*t41) + 2*fo*dtg2
    t52n = (1-4*fo)*t52+fo*(t42+t62+2*t51) + 2*fo*dtg2
    t62n = (1-4*fo)*t62+fo*(t52+t72+2*t61) + 2*fo*dtg2
    t72n = (1-4*fo)*t72+fo*(t62+t82+2*t71) + 2*fo*dtg2
    t82n = (1-4*fo)*t82+fo*(t72+t92+2*t81) + 2*fo*dtg2
    t92n = (1-4*fo)*t92+fo*(t82+t102+2*t91) + 2*fo*dtg2
    t102n = (1-4*fo)*t102+fo*(2*t92+2*t101) + 2*fo*dtg2
    # roll values
    t11, t21, t31, t41, t51, t61, t71, t81, t91, t101 = t11n, t21n, t31n, t41n, t51n, t61n, t71n, t81n, t91n, t101n
    t12, t22, t32, t42, t52, t62, t72, t82, t92, t102 = t12n, t22n, t32n, t42n, t52n, t62n, t72n, t82n, t92n, t102n
    if 1740<t102<1741:
        print('number of time steps: ', i+1)
        print(t102)
