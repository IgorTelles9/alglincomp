import p2_task1;

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
