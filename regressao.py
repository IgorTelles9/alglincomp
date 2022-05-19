from sympy import var
from sympy import sympify
from utils import getTranspose, multiplyMatrices, matrixToVec, vecToMatrix
import lu
import substitution

def regressao(npares, xcord, ycord, func, xpred):
    '''
    Calcula a coordenada y dada um xpred alvo de uma funcao ajustada 
    a coordenadas xcord e ycord. xcord e ycord são vetores, func é a 
    funcao alvo em string (linguagem matematica do python, sempre 
    separando fatores por '+') e npares é a quantidade de pares
    fornecidos
    '''

    # transforma o vetor ycord em uma matriz

    ycord = vecToMatrix(ycord)

    x = var('x')  
    funcs = func.split('+')

    p = []
    # inicializa a matriz p
    for i in range(npares):
        p.append([])

    # inicializa a matriz b
    b = []

    # itera para cada função menor na funcao de input
    for pequena in funcs:
        expr = sympify(pequena)

        for k in range(npares):
            p[k].append(expr.subs(x, xcord[k]))
            
    # calcula PTxP
    a = multiplyMatrices(getTranspose(p), p)

    # calcula PTxY
    c = multiplyMatrices(getTranspose(p), ycord)

    # transforma em vetor
    c = matrixToVec(c)

    ordem = len(c)

    # resolve o sistema de equacoes usando LU
    a = lu.decomposition(a, ordem)
    y = substitution.foward(a , c, ordem)
    r = substitution.back(a , y, ordem)

    ypred = 0
    # avalia o xpred nas nas expressoes desejadas com os coeficientes obtidos
    for i,coef in enumerate(r):
        expr = sympify(funcs[i])
        ypred += coef*expr.subs(x, xpred)


    return ypred
