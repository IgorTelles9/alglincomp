f = lambda vars: vars[0]+vars[1]-5
g = lambda vars: vars[0]**2+vars[1]**2-25
s = [f,g]

x = 0.1
h = 0.001


def first_order(f, x, h, option=2,hasParams=False, params=0):
    """ 
        option: 0 = passo a frente 
        option: 1 = passo atrás
        option: 2 = diferença central

        hasParams: define if the function has variable params (used in task 2)
    """
    if hasParams:
        if option == 0:
            return (f(params,x+h) - f(params,x))/(h)
        elif option == 1:
            return (f(params,x) - f(params,x-h))/(h)
        elif option == 2:
            return (f(params,x+h) - f(params,x-h))/(2*h)
    else:
        if option == 0:
            return (f(x+h) - f(x))/(h)
        elif option == 1:
            return (f(x) - f(x-h))/(h)
        elif option == 2:
            return (f(x+h) - f(x-h))/(2*h)

def partial(f, vars, h):
    partials = []
    vars_p = vars[:]
    vars_m = vars[:]
    for i in range(len(vars)):
        vars_p[i] = vars[i] + h
        vars_m[i] = vars[i] - h
        partials.append((f(vars_p) - f(vars_m))/(2*h))
        vars_p = vars[:]
        vars_m = vars[:]
    return partials

def jacobian(s,vars,h):
    j = []
    for f in s:
        j.append(partial(f,vars,h))
    return j