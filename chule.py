
from math import prod, sqrt
from pprint import pprint 

def cholesky(A, ordem, idet=False):
    # Quantidade de linhas/colunas da matriz A
    

    # Inicializar L com um bando de 0s
    L = [[0.0] * ordem for i in range(ordem)] 

    # Iteração planejada de modo a formar L[i][k] como uma inferior
    for i in range(ordem):
        for k in range(i+1):   

            soma_tmp = sum(L[i][j] * L[k][j] for j in range(k))   

            if (i == k):
                check = A[i][i] - soma_tmp
                if check <= 0:
                    return 'deu merda', 'deu merda'                                 
                L[i][k] = sqrt(check)     

            else:    
                denominador = L[k][k] * (A[i][k] - soma_tmp) 
                if denominador == 0:
                    return 'deu merda', 'deu merda'                          
                L[i][k] = (1.0 /denominador)
    if idet:
        det = (prod(L[j][j] for j in range(ordem)))**2
    else:
        det = 'Determinante não calculado'
    return L, det

A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
L, det = cholesky(A, 1)

print("A:")
pprint(A)

print("L:")
pprint(L)

pprint(det)