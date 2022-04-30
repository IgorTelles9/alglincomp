from lu import luDecomposition
from utils import printMatrix, printVector
import substitution 

m1 = [[5, -4, 1, 0], [-4, 6, -4, 1], [1, -4, 6, -4], [0, 1, -4, 5]]
m2 = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]
v1 = [-1,2,1,3]
v2 = [3,6,10]

size = len(m1)

print('matriz inicial:')
printMatrix(m1)
lu = luDecomposition(m1, size)
print('matriz lu:')
printMatrix(lu)
y= substitution.foward(lu,v1,size)
print('vetor y:')
printVector(y)
x = substitution.back(lu, y, size)
print('vetor x:')
printVector(x)