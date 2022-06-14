import norm
def seidel(matrix, vector, ordem, tolm):
    # solucao inicial
    y = [1]*ordem 
  
    # solucao que sera calculada
    w = [0]*ordem

    # tolm em notacao cientifica
    tolm_nc = float('1e-'+str(tolm))
  
    # flag para controlar iteracao 
    halt = False

    # list com historico de erros
    error = []
    
    counter = 0

    while not halt:
        counter += 1
    # loop que itera para cada elemento do novo vetor de solução
        for i in range(ordem):

            sum1 = 0
            sum2 = 0
            # primeiro somatorio da formula
            for j in range(i-1):
                sum1 += matrix[i][j] * w[j]
            
            # segundo somatório da fórmula
            for j in range(i+1, ordem):
                sum2 += matrix[i][j] * y[j]

            w[i] = (vector[i] - sum1 - sum2)/matrix[i][i]

    # calculo do residuo
    diff = [0]*ordem
    for i in range(ordem):
      diff[i] = round( (w[i]-y[i]), tolm)
    try:
     r = round ( (norm.euclidian(diff,tolm)/norm.euclidian(w, tolm)), tolm) 
     error.append(r)
    except OverflowError:
      halt = True
      
    # analise da tolerancia e residuo 
    if (r <= tolm_nc or halt):
      halt = True
    else:
      y = w[:] 
    return w,counter,error



