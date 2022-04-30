from lu import luDecomposition
from utils import printMatrix
import substitution 

m1 = [[5, -4, 1, 0], [-4, 6, -4, 1], [1, -4, 6, -4], [0, 1, -4, 5]]
m2 = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]
v1 = [-1,2,1,3]
v2 = [3,6,10]

lu = luDecomposition(m2, 3)
printMatrix(lu)
y= substitution.foward(lu,v2,3)
print(y)
x = substitution.back(lu, y, 3)
print(x)