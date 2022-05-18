from turtle import onkeypress
import substitution
import lu
import utils 
import determinant
import jacobi
import gausseidel
from chule import cholesky

loop = True 

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE SISTEMAS LINEARES')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa resolve sistemas lineares utilizando os seguintes métodos:')
print()

utils.displayMetodos()

while loop:
  (ordem, icod, idet, arquivo_a, arquivo_b, tolm) = utils.configura()

  matriz = utils.getMatrix(arquivo_a)
  vetor = utils.getMatrix(arquivo_b)
  x = []
  det = 0
  itCounter = 0
  error = []

  # ############### resolucao do sistema ####################
  # ############ decomposicao LU ###############
  if icod == 1:
    matriz_lu = lu.decomposition(matriz, ordem)
    y = substitution.foward(matriz_lu , vetor, ordem)
    x = substitution.back(matriz_lu , y, ordem)
    
    # ########### calculo do determinante ###############
    if idet > 0:
      det = determinant.getTriangular(matriz_lu,ordem)
    # ########### fim calculo do determinante ###############
    
  # ############ fim decomposicao LU ###############
  

  # ############ metodo de cholesky ############### 

  if icod == 2:
    matriz_cholesky, det = cholesky(matriz, ordem, idet)
    # Ainda tem que fazer o chulé devolver a transposta
    # Ele tem que identificar quando a matriz é não simetrica positiva definida?
    

  # ############ fim do metodo de cholesky ############### 


  # ############ metodo de jacobi ############### 
  if icod == 3: 
    if not jacobi.converge(matriz, ordem):
      print()
      print('ATENCAO:')
      print('A matriz NAO e diagonal dominante.')
      print('Portanto NAO ha garantia de CONVERGENCIA para o metodo de Jacobi.')
      
    x, itCounter, error = jacobi.method(matriz, vetor, ordem, tolm)
  # ############ fim metodo de jacobi ############### 
  
  # ############ metodo de gauss-seidel ############### 

  if icod == 4: 
    if not jacobi.converge(matriz, ordem):
      print()
      print('ATENCAO:')
      print('A matriz NAO e diagonal dominante.')
      print('Portanto NAO ha garantia de CONVERGENCIA para o metodo de Jacobi.')
      
    x, itCounter, error = gausseidel.seidel(matriz, vetor, ordem, tolm)

  # ############ fim do metodo de gauss-seidel ############### 

  # ############### fim resolucao do sistema ####################
  

  # ############## resultados ##################
  print('Vetor X:')
  utils.printVector(x)
  if idet > 0:
    print('Determinante:')
    print(det)
    print()

  if icod == 2:
    print('Matriz da decomposição de Cholesky:')
    print(matriz_cholesky)
    print('Determinante:')
    print(det)

  if icod == 3 or icod == 4:
    print('Numero de iteracoes: %s'  % (itCounter))
    print()
    print('Historico da variacao do erro: ')
    print(error)
    print()
  # ############## fim resultados ##################
  
  again = input('Gostaria de resolver outro sistema? (s para sim) ')
  if again != 's':
    loop = False 
    
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
