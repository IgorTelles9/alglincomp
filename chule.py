from math import prod, sqrt
from pprint import pprint 
from utils import getTranspose

def cholesky(A, ordem, idet=False):
    # Quantidade de linhas/colunas da matriz A
    
    L =[]
    # Inicializar L com um bando de 0s
    for i in range(ordem):
        L.append([])
        for k in range(ordem):
            L[i].append(0.0)

    # Iteração planejada de modo a formar L[i][k] como uma inferior
    for i in range(ordem):
        for k in range(i+1):   
            
            soma_tmp = sum(L[i][j] * L[k][j] for j in range(k))   

            if (i == k):
                check = A[i][i] - soma_tmp
                if check < 0:
                    print('matriz nao ta certa', 'matriz nao ta certa')   
                                                 
                L[i][k] = sqrt(check)     

            else:    
                denominador = L[k][k] * (A[i][k] - soma_tmp) 
                denominador = L[i][i]
                if denominador == 0:
                    print('matriz nao ta certa', 'matriz nao ta certa')  
                    #return 0,0,0                        
                L[k][i] = (1.0 /denominador)
    if idet:
        det = (prod(L[j][j] for j in range(ordem)))**2
    else:
        det = 'Determinante não calculado'

    Lt = getTranspose(L)
    return L, Lt, det
