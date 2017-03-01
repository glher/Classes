'''
   Discrete derivative calculations
   Runs under Python 2.7
'''
import math

def g(x):
    return math.sin(x)

def f(x):
    return (x**3-2.)/(x*x+1)

def gderiv(x):
    return math.cos(x)

def fderiv(x,order):
    if order == 1:
        return x*(x**3+3*x+4.)/(1.+x*x)**2
    if order == 2:
        return -2.*(-2.+x*(-3.+x*(6.+x)))/(x*x+1.)**3
 
def firstderiv(x,h):
    forward=(f(x+h)-f(x))/h
    backward=(f(x)-f(x-h))/h
    centered=0.5*(f(x+h)-f(x-h))/h
    centered2=(f(x-2.*h)-8.*f(x-h)+8.*f(x+h)-f(x+2.*h))/(12.*h)
    return forward, backward, centered, centered2

def secondderiv(x,h):
    centered1=(f(x+h)-2.*f(x)+f(x-h))/h**2
    centered2=(-f(x-2.*h)+16.*f(x-h)-30.*f(x)+16.*f(x+h)-f(x+2.*h))/(12.*h**2)
    return centered1, centered2

def main():
    xlist=[1.2,1.7,2.2]
    for j in range(3):
         x = xlist[j]
         print 'x=',x
         exact=fderiv(x,1)         
#         exact=gderiv(x)
         for j in range(1,4):
            h=10**(-j)
            for1, back1, cent1, cent12 = firstderiv(x,h)
            print 'h =',h
            print 'error in forward, backward, cent., centered2 estimates:', \
                   for1-exact, back1-exact, cent1-exact, cent12-exact
    xlist2=[2.3,2.7,3.1]
    for j in range(3):
         x = xlist2[j]
         print 'x=',x
         exact2=fderiv(x,2)         
         for j in range(1,4):
            h=10**(-j)
            cent12, cent22 = secondderiv(x,h)
            print 'h =',h
            print 'error in 2nd derivative estimates:', \
                   cent12-exact2, cent22-exact2
            

main()
