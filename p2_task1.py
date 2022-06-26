import lu
import substitution
import derivative 
import norm
import utils
from copy import deepcopy

def calc_functions(s,x):
    f = []
    for func in s:
        f.append(func(x)*-1) # eu nao lembro pq multiplica por -1
    return f


def newton(s,x,tolm,itmax):
    order = len(s)
    for _ in range(itmax):
        f = calc_functions(s,x)
        jacobian = derivative.jacobian(s,x,tolm)
        print(jacobian)
        
        # solving system
        lu_matrix = lu.decomposition(jacobian, order)
        y = substitution.foward(lu_matrix,f, order)
        delta_x = substitution.back(lu_matrix, y, order)
        
        # new value
        x_new = [x[i] + delta_x[i] for i in range(order)]

        # analizing stop condition
        tolk = norm.euclidian(delta_x) / norm.euclidian(x_new)

        if (tolk > tolm):
            x = deepcopy(x_new)
        else:
            return [round(x,2) for x in x_new ]
    raise ValueError('The iteration max was reached.')

def broyden(s,x,tolm,itmax):
    order = len(s)
    jacobian = derivative.jacobian(s,x,tolm)

    for _ in range(itmax):

        # applying x in the function
        f = calc_functions(s,x)

        # solving system
        lu_matrix = lu.decomposition(deepcopy(jacobian), order)
        y = substitution.foward(lu_matrix,f, order)
        delta_x = substitution.back(lu_matrix, y, order)

        x_new = [x[i] + delta_x[i] for i in range(order)]

        f_new = calc_functions(s,x_new)
        y = [f_new[i] - f[i] for i in range(order)]

        tolk = norm.euclidian(delta_x) / norm.euclidian(x_new)

        if (tolk > tolm):
            # new jacobian 
            delta_x_column = utils.vecLineToColumn(delta_x)
            y_column = utils.vecLineToColumn(y)
            j1 = utils.multiplyMatrices(jacobian,delta_x_column)
            j2 = utils.addMatrices(y_column, j1)
            j3 = utils.multiplyVectors(j2,delta_x)
            j4 = utils.multiplyVectors(delta_x, delta_x_column,False)
            j5 = utils.multiplyByValue(j3,1/j4)
            jacobian = utils.subtractMatrices(deepcopy(jacobian), j5)

            x = deepcopy(x_new)
            
        else:
            return [round(x,2) for x in x_new ]
    raise ValueError('The iteration max was reached.')

