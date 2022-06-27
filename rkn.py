import math

def func(t,y,yl,a1,a2,a3,w1,w2,w3,m,c,k):
    return ((-c*yl)-(k*y)+(a1*math.sin(w1*t))+(a2*math.sin(w2*t))+(a3*math.cos(w3*t)))/m


def rkn(h,temp,a1,a2,a3,w1,w2,w3,m,c,k):

    t=0
    y=0
    yl=0
    
    while t <= temp:
        k1 = 0.5*h*func(t,y,yl,a1,a2,a3,w1,w2,w3,m,c,k)
        q = 0.5*h*(yl+0.5*k1)
        k2 = 0.5*h*func(t+(h/2),y+q,yl+k1,a1,a2,a3,w1,w2,w3,m,c,k)
        k3 = 0.5*h*func(t+(h/2),y+q,yl+k2,a1,a2,a3,w1,w2,w3,m,c,k)
        l = h*(yl+k3)
        k4 = 0.5*h*func(t+h,y+l,yl+2*k3,a1,a2,a3,w1,w2,w3,m,c,k)

        y = y + h*(yl+(1/3)*(k1+k2+k3))
        yl = yl + (1/3)*(k1+2*k2+2*k3+k4)
        t += h
        t = round(t,1)
        
    return y, yl

#print(rkn(0.1,10,1,2,1.5,0.05,1,2,1,0.1,2))
