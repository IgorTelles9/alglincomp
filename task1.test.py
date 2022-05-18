import pprint
# import lu
# from utils import printMatrix, printVector
# import substitution
# import jacobi
from chule import cholesky

m1 = [[5, -4, 1, 0], [-4, 6, -4, 1], [1, -4, 6, -4], [0, 1, -4, 5]]
m2 = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]
m3 = [[3, -1, -1], [-1, 3, -1], [-1, -1, 3]]
v1 = [-1, 2, 1, 3]
v2 = [3, 6, 10]
v3 = [1, 2, 1]


# jacobi.method(m3,v3,3,3)
# printVector(jacobi.method(m3,v3,3,3))

# size = len(m1)

# print('matriz inicial:')
# printMatrix(m1)

# lu = lu.decomposition(m1, size)
# print('matriz lu:')
# printMatrix(lu)

# print('vetor b:')
# printVector(v1)

# y= substitution.foward(lu,v1,size)
# print('vetor y:')
# printVector(y)

# x = substitution.back(lu, y, size)
# print('vetor x:')
# printVector(x)

A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
L, det = cholesky(A, 1)

print("A:")
pprint(A)

print("L:")
pprint(L)

pprint(det)
