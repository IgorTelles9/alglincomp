import lu
import substitution
import derivative 
import norm

def calc_functions(s,x):
    f_calc = []
    for f in s:
        f_calc.append(f(x)*-1)
    return f_calc


def method(s,x,tolm,itmax):
    order = len(s)
    for i in range(itmax):
        f_calc = calc_functions(s,x)
        jacobian = derivative.jacobian(s,x,tolm)

        
        # solving system
        lu_matrix = lu.decomposition(jacobian, order)
        y = substitution.foward(lu_matrix,f_calc, order)
        z = substitution.back(lu_matrix, y, order)
        
        # new value
        x_new = [x[i] + z[i] for i in range(order)]

        # analizing stop condition
        tolk = norm.euclidian(z) / norm.euclidian(x_new)

        # print('Iteration:\t %d' %(i))
        # print('Jacobian:\t' + str(jacobian))
        # print('x_new:\t\t' + str(x_new))
        # print('delta x:\t' + str(z))
        # print('tolk:\t %f' %(tolk))

        if (tolk > tolm):
            x = x_new[:]
        else:
            return [round(x,2) for x in x_new ]
    raise ValueError('The iteration max was reached.')