# initialize guesses
x1, x2, x3, x4 = 0., 0., 0., 0.
# iterate:
for i in range(10):
    x1=(10.-3.*x2-5.*x3-2.*x4)/(-1.)
    x2=(15-x1-8.*x3-4.*x4)/9.
    x3=(-3.-2.*x1-x2+x4)/1.
    x4=(2.-x2)/1.
    print(x1, x2, x3, x4)
print('solution:')
print(x1, x2, x3, x4)

x1, x2, x3, x4 = 0., 0., 0., 0.
# iterate:
for i in range(50):
    x1=(-3.-x2-x3+x4)/2.
    x2=(15-x1-8.*x3-4.*x4)/9.
    x3=(10+x1-3.*x2-2.*x4)/5.
    x4=(2.-x2)/1.
    print(x1, x2, x3, x4)
print('solution:')
print(x1, x2, x3, x4)
