from math import exp
import p2_task1;
import p2_task2;
import derivative;

# TASK 1 

def task1(icod, params, x, tolm):
    f = lambda vars: 2*vars[1]**2 + vars[0]**2 + 6*vars[2]**2 -1.0
    g = lambda vars: 8*vars[1]**3 + 6*vars[1]*vars[0]**2 + 36*vars[1]*vars[0]*vars[2] + 108*vars[1]*vars[2]**2 - params[0]
    h = lambda vars: 60*vars[1]**4 + (60*vars[1]**2)*(vars[0]**2) + (576*vars[1]**2)*vars[0]*vars[2] + \
        (2232*vars[1]**2)*(vars[2]**2) + (252*vars[2]**2)*vars[0]**2 + (1296*vars[2]**3)*vars[0] + \
        3348*vars[2]**4 + (24*vars[0]**3)*vars[2] + 3*vars[0] - params[1]
    s = [f,g,h]
    # f = lambda vars: vars[0] + 2*vars[1] - 2 
    # g = lambda vars: vars[0]**2 + 4*vars[1]**2 - 4
    # s=[f,g]

    if icod == 1:
        return p2_task1.newton(s,x,tolm,100)
    elif icod == 2:
        return p2_task1.broyden(s,x,tolm,100)
for i in range(1,3,1):
    print('ICOD = %i' %i)
    print(task1(i,[0.00,3.00],[1,0,0],0.0001))
    print(task1(i,[0.75,6.5],[1,0,0],0.0001))
    print(task1(i,[0.00,11.667],[1,0,0],0.0001))

def task2(icod, params, tolm,a=0,b=0,delta_x=0,opcao_der=0):
    f = lambda vars,x: vars[0]*exp(vars[1]*x) + vars[2]*x**vars[3]

    if icod == 1:
        return p2_task2.bissection(a,b,tolm,f,params)
    elif icod == 2:
        pass
    elif icod == 3: 
        derivative.first_order(f,a,delta_x,opcao_der,True,params)
    elif icod == 4:
        pass

# print(task2(3,[-4,0,2,2], 0.001,2,2,0.0001,0))
