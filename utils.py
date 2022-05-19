from wr_utils import printMatrix


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
    Return the resultant matrix of a square matrices multipication
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
    '''
    Returns the resultant vector of a matrix-vector multiplication.
    @param m,v 
    @returns x the resultant vector
    '''
    x = [0.0 for i in range(len(v))]
    for i in range(len(m)):
        for j in range(len(m)):
            x[i] += m[i][j]*v[j]
    return x

def isSymmetric(m, order):
    '''
    @returns true if the matrix is symmetric
    '''
    control = [[False for j in range(order)] for i in range(order)]
    for i in range(order):
        for j in range(order):
            if i!=j and not control[i][j]:
                if m[i][j] != m[j][i]:
                    return False 
                else:
                    control[i][j] = control[j][i] = True
    return True 
def getTranspose(matrix):
  trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  return trans

def multiplyMatrices(m1,m2):

  nlinhas = len(m1)
  ncolunas = len(m2[0])
  result = []

  # Criacao da matriz resultado cheia de 0s
  for linhas in range(nlinhas):
    result.append([])
    for colunas in range(ncolunas):
      result[linhas].append(0)

  for i in range(nlinhas):
   
    for j in range(ncolunas):
       
      for k in range(len(m2)):
        result[i][j] += m1[i][k] * m2[k][j]

  return result

def matrixToVec(matrix):
  vec = []
  for i in range(len(matrix)):
    vec.append(matrix[i][0])

  return vec

def vecToMatrix(vec):
  matrix = []
  for i in range(len(vec)):
    matrix.append([])
    matrix[i].append(vec[i])
  
  return matrix
