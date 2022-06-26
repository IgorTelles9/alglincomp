from math import cos, exp
from re import X

def bissection(a,b,tol,f,vars):
    while abs(b-a) > tol:

        x = (a+b)/2
        f_i = f(vars,x)

        if f_i > 0.0:
            b = x 
        else: 
            a = x 

    return x 