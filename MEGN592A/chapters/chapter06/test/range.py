# -*- coding: utf-8 -*-

#import matplotlib.pyplot as plt
import numpy as np 
import math 
import scipy.constants as const 

g = const.g #gravitation constant 
dt = 1e-3 #integration time step (delta t) 
v0 = 50 #initial speed at t=0 
angle = math.pi / 4 #launch angle in radians 
time = np.arange(0,100, dt) #create time axis 
gamm = 0.0005 #gamma (used to compute f, below) 
h = 100 #height (used to compute f, below) 

def traj_fr(angle, v0):
#function that computes trajectory for some launch angle & velocity 
    vx0 = math.cos(angle)*v0 #compute x components of starting velocity
    vy0 = math.sin(angle)*v0 #compute y components of starting velocity
    x = np.zeros(len(time)) #initialise x array
    y = np.zeros(len(time)) #initialise y array
    x[0],y[0] = 0,0 #initial position at t=0s, ie motion starts at (0,0)
    x[1],y[1] = x[0] + vx0*(2*dt), y[0]+vy0*(2*dt) #calculating 2nd elements of x & y based on init velocity
    i=1
    while y[i]>=0:
    #loop continuous until y becomes <0, ie projectile hits ground
        f = gamm * dt #intermediate 'function'; used in calculating x & y vals below
        x[i+1] = ((2*x[i]-x[i-1]) + (f * x[i-1])) / (1 + f) #numerical integration to find x[i+1]...
        y[i+1] = ((2*y[i]-y[i-1]) + (f * y[i-1]) - g*(dt**2) ) / (1 + f) # ...& y[i+1]
        i = i+1 #increment i for next iteration
    x = x[0:i+1] #truncate x array
    y = y[0:i+1] #truncate y array
    print(x)
    return x, y, (dt*i), x[i] #return x, y, flight time, range of projectile

x,y,duration,distance = traj_fr(angle,v0) #define variables for output of traj_fr function
print('Distance: ' , distance)
print('Duration: ' , duration)
n = 5
angles = np.linspace(0, math.pi/2, n) #generate array of n angles
print('Angles: ' , angles)
maxrange = np.zeros(n) #generate array of n elements to take range from traj_fr

for i in range(n):
#loop to run angles through traj_fr function & populate maxrange array with distance results
    x,y,duration,maxrange[i] = traj_fr(angles[i], v0)
angles = angles / 2 / math.pi * 360 #convert radians to degrees
print('Launch Angles: ', angles)
print('Optimum Angle: ', angles[np.where(maxrange==np.max(maxrange))])
#plt.plot(x,y) #quick plot of x vs y to check trajectory
#plt.xlabel('x')
#plt.ylabel('y')


