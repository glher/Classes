'''
   Gauss-Seidel iterative solution for cruciform heat conduction example
'''   

# initialize guesses
t1, t2, t3, t4, t5, t6 = 500., 500., 500., 500., 500., 500.
print 'temperature solution (degrees F):'
# iterate:
for i in range(16):
    t1=t2+35
    t2=.25*(t1+t3)+335.
    t3=.25*(t2+t4)+335.
    t4=.25*(t3+t5)+335.
    t5=.25*(t4+t6)+335.
    t6=.25*t5+485.
    if i % 5 == 0:
        print 'number of iterations: ', i+1
        print t1, t2, t3, t4, t5, t6
        print 
