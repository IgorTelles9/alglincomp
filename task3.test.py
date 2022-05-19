import numpy as np
from interpolacao import interpola
from regressao import regressao
from utils import multiplyMatrices, getTranspose, vecToMatrix
import lu
import substitution

#print(np.polynomial.polynomial.polymul((1,-1), (-4,1)))

#print(interpola(2,[1,-7],[11,67], 2))

from sympy import var
from sympy import sympify

p = [[1,1],[1,2],[1,3]]
y = [[2],[3.5],[6.5]]


print(getTranspose(p))
a = multiplyMatrices(getTranspose(p), p)
c = multiplyMatrices(getTranspose(p), y)
print(multiplyMatrices(a, c))

x = var('x')  # the possible variable names must be known beforehand...
user_input = 'x * sin(x**2)'
expr = sympify(user_input)
res = expr.subs(x, 3.14)
print(res)  # -1.322...

x = [1,2,3]
y = [2,3.5,6.5]


print(regressao(3,x,y,'1+x',1))


##print('matriz lu:')
#printMatrix(lu)

##print('vetor b:')
#printVector(v1)

#y= substitution.foward(lu,v1,size)
#print('vetor y:')
#printVector(y)