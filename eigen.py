from math import pi, sin, cos, atan
from utils import getIdentity, multiplySquareMatrix, multiplyMatrixVector

def power_method(matrix, order, tolm):
    '''
    Calculates the biggest eigenvalue and its associated eigenvector.
    @param matrix, order, tolm
    @returns value, vector, counter
    '''
    vector = [1.0 for i in range(order)]
    value = 1.0
    counter = 0
    tolm_nc = float('1e-'+str(tolm))
    halt = False 
    while(not halt):
        vector = multiplyMatrixVector(matrix, vector)
        prev_value = value 
        value = max(vector)
        vector = [item/value for item in vector]
        r = abs(value - prev_value)/value 
        counter+=1
        
        if (r <= tolm_nc):
            halt = True
    value = round(value,tolm)
    vector = [round(item, tolm) for item in vector]
    return value, vector, counter

def jacobi(matrix, order, tolm):
    '''
      Calculates the eigenvectors and eigenvalues for symmetric matrices.
      @param matrix, order, tolm
      @returns matrix, vectors, counter
    '''
    vectors = getIdentity(order)
    halt = False
    tolm_nc = float('1e-'+str(tolm))
    counter = 0

    while(not halt):
        # getting max out-diagonal value
        max_value = 0
        max_i = -1
        max_j = -1
        for i in range(order):
            for j in range(order):
                if(i != j and abs(matrix[i][j]) > abs(max_value)):
                    max_value = matrix[i][j]
                    max_i = i
                    max_j = j

        # setting theta
        m_ii = matrix[max_i][max_i]
        m_jj = matrix[max_j][max_j]
        if(m_ii == m_jj):
            theta = pi/4
        else:
            theta = (1/2) * atan((2*matrix[max_i][max_j]) / (m_ii - m_jj))

        # setting p matrix
        p = getIdentity(order)
        p[max_j][max_i] = sin(theta)
        p[max_i][max_j] = p[max_j][max_i] * -1
        p[max_i][max_i] = p[max_j][max_j] = cos(theta)

        # operations over the matrix
        matrix = multiplySquareMatrix(p, matrix, tolm, m1_t=True)
        matrix = multiplySquareMatrix(matrix, p, tolm)
        vectors = multiplySquareMatrix(vectors, p, tolm)
        
        counter += 1

        # check if values are under tolm
        halt = True
        for i in range(order):
            for j in range(order):
                if (i != j and halt):
                    if (abs(matrix[i][j]) > tolm_nc):
                        halt = False

    # rounding for display
    for i in range(order):
        for j in range(order):
            matrix[i][j] = round(matrix[i][j], tolm)
            vectors[i][j] = round(vectors[i][j], tolm)

    return matrix, vectors, counter
