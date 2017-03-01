# initialize guesses
x1, x2, x3, x4 = 0., 0., 0., 0.
# iterate:
for i in range(50):
    x1=(-3.-x2-x3+x4)/2.
    x2=(15-x1-8.*x3-4.*x4)/9.
    x3=(10+x1-3.*x2-2.*x4)/5.
    x4=(2.-x2)/1.
print 'solution:'
print x1, x2, x3, x4
