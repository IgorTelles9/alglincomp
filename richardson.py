import math

def richardson(vec, delta1, delta2, a):
    c1,c2,c3,c4 = vec
    d1 = ( ((c1*(math.e**(c2*(a+delta1))))+(c3*((a+delta1)**c4))) - ((c1*(math.e**(c2*(a))))+(c3*((a)**c4))) ) / delta1
    d2 = ( ((c1*(math.e**(c2*(a+delta2))))+(c3*((a+delta2)**c4))) - ((c1*(math.e**(c2*(a))))+(c3*((a)**c4))) ) / delta2
    q = delta1/delta2
    print(d1,d2,q)
    derivada = d1 + ((d1-d2)/((q**(-1))-1))

    return derivada


print(richardson([2,6,1.5,4],0.5,0.25,-1))
