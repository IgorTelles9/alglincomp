import newton;

# TASK 1 

def task1(icod, params, x, tolm):
    f = lambda vars: 2*vars[1]**2 + vars[0]**2 + 6*vars[2]**2 -1.0
    g = lambda vars: 8*vars[1]**3 + 6*vars[1]*vars[0]**2 + 36*vars[1]*vars[0]*vars[2] + 108*vars[1]*vars[2]**2 - params[0]
    h = lambda vars: 60*vars[1]**4 + (60*vars[1]**2)*(vars[0]**2) + (576*vars[1]**2)*vars[0]*vars[2] + \
        (2232*vars[1]**2)*(vars[2]**2) + (252*vars[2]**2)*vars[0]**2 + (1296*vars[2]**3)*vars[0] + \
        3348*vars[2]**4 + (24*vars[0]**3)*vars[2] + 3*vars[0] - params[1]
    s = [f,g,h]

    if icod == 1:
        return newton.method(s,x,tolm,100)

print(task1(1,[0.00,3.00],[1,0,0],0.0001))
print(task1(1,[0.75,6.5],[1,0,0],0.0001))
print(task1(1,[0.00,11.667],[1,0,0],0.0001))
