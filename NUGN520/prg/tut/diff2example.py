'''
  function as argument of function example
'''
import math

def diff2(f,x,h=1e-6):              #note how we may set a default value for h
    return (f(x-h)-2.*f(x)+f(x+h))/float(h*h)

def g(t):
    return t**(-6)

for k in range(1,15):
    h = 10**(-k)
    d2g = diff2(g, 1, h)
    print 'h=%.0e: %.5f' % (h, d2g)

# Lambda function example
d2 = diff2(lambda t: t**(-6), 1, h=1e-4)
print d2
d22 = diff2(lambda t, A=1, a=0.5: -a*2*t*A*math.exp(-a*t**2), 1.2,1e-4)
print d22


