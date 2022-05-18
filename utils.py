def getIdentity(order):
    '''
    Return the identity matrix of the given order
    '''
    m = [[0.0 for j in range(order)] for i in range(order)]
    for i in range(order):
        for j in range(order):
            if (i == j):
                m[i][i] = 1.0
    return m


def multiplySquareMatrix(m1, m2, tolm, m1_t=False, m2_t=False):
    '''
    Return the result matrix of a square matrices multipication
    @param m1, m2 are the matrices
    @param m1_t, m2_t defines if that matrix should be transposed
    '''
    order = len(m1)
    m = [[0.0 for j in range(order)] for i in range(order)]
    for i in range(order):
        for j in range(order):
            for k in range(order):
                if (m1_t and m2_t):
                    m[i][j] += (m1[k][i] * m2[j][k])
                elif(m1_t):
                    m[i][j] += (m1[k][i] * m2[k][j])
                elif(m2_t):
                    m[i][j] += (m1[i][k] * m2[j][k])
                else:
                    m[i][j] += (m1[i][k] * m2[k][j])
    return m


def multiplyMatrixVector(m, v):
    x = [0.0 for i in range(len(v))]
    for i in range(len(m)):
        for j in range(len(m)):
