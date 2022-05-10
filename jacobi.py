from xmlrpc.client import boolean
import norm

def method(matrix, vector, ordem,tolm):
  '''
    Calcula a solucao de um sistema linear utilizando o Método Iterativo de Jacobi.
    
    @param tolm é a tolerancia máxima de erro. 
  '''
  
  # solucao inicial
  y = [1]*ordem 
  
  # solucao que sera calculada
  w = [0]*ordem
  
  # tolm em notacao cientifica
  tolm_nc = float('1e-'+str(tolm))
  
  # flag para controlar iteracao 
  halt = False 
  
  # numero de iteracoes necessarias
  counter = 1
  
  # list com historico de erros
  error = []
  
  while (not halt):
    counter += 1
    
    # calculo da nova solucao iterativa (w)
    for i in range(ordem):
      w[i] = vector[i]
      for j in range(ordem):
        if (i != j):
          w[i] -= round ( (matrix[i][j]*y[j]), tolm)
      w[i] = round((w[i]/matrix[i][i]),tolm)
    
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

def converge(matrix: list, ordem: int):
  ''' 
    Verifica se há garantia para convergência do método de jacobi.
    Para isso, checa se a matriz é diagonal dominante.
  '''
  for i in range(ordem):
    sum_line= 0
    sum_column = 0
    for j in range(ordem):
      if i != j:
        sum_line += abs(matrix[i][j])
        sum_column += abs(matrix[j][i])
    if (matrix[i][i] < sum_line or matrix[i][i] < sum_column):
      return False
  return True 
  
