def back(upper, vector, size):
    ''' 
        Aplica o algoritmo de substituição para trás em uma matriz. 
    '''
    x = size*[0.0]
    for i in range(size-1, -1, -1):
        for j in range(size-1, i-1, -1):
            if (i == j):
                x[i] = round(((vector[i] - x[i])/upper[i][i]), 2)
            else:
                x[i] += round((x[j] * upper[i][j]), 2)
    return x


def foward(lower, vector, size, trueLower = False):
    '''' 
        Aplica o algoritmo de substituição para frente em uma matriz.
        
        Se o @param lower for de fato uma matriz inferior, @param trueLower deve 
        ser passado como True.
        Mas se o @param lower for uma matriz L e U combinadas, vinda de uma
        decomposição LU, @param trueLower deve ser mantido False. 
    
    '''
    x = size*[0.0]
    for i in range(size):
        x[i] = round((vector[i]), 2)
        for j in range(0, ((size+1+i)-size), 1):
            if (i != j):
                x[i] -= round((x[j]*lower[i][j]), 2)
                x[i] = round((x[i]), 2)
            elif trueLower:
                x[i] = round( (x[i]/i),2)
                
    return x
