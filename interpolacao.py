import numpy as np

def interpola(nvalores, xcord, ycord, xpred):

    func = 0
    # itera para cada parcela da funcao final
    for i in range(nvalores):

        # resultado do produtório numerador da formula
        prod1 = 1

        # resultado do produtorio denominador da formula
        prod2 = 1

        # produtório numerador da formula
        for k in range(nvalores):
            if k != i:
                prod1 = np.polynomial.polynomial.polymul((-xcord[k], 1), prod1)
            else:
                pass

        # produtorio denominador da formula
        for k in range(nvalores):
            if k != i:
                prod2 *= xcord[i] - xcord[k]

        # divisao dos produtórios vezes yi
        div = ycord[i] * np.polydiv(prod1, prod2)[0]

        # soma à funcao final
        func = np.polyadd(func, div)

    # calcula o y previsto para dado x
    ypred = 0
    for pot, coef in enumerate(func):
        ypred += coef * xpred**pot

    return ypred
