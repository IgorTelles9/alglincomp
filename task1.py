from turtle import onkeypress
import substitution
import lu
import utils 
import determinant
import jacobi

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
  
  # ############ metodo de jacobi ############### 
  if icod == 3: 
    if not jacobi.converge(matriz, ordem):
      print()
      print('ATENCAO:')
      print('A matriz NAO e diagonal dominante.')
      print('Portanto NAO ha garantia de CONVERGENCIA para o metodo de Jacobi.')
      
    x, itCounter, error = jacobi.method(matriz, vetor, ordem, tolm)
  # ############ fim metodo de jacobi ############### 
  
  # ############### fim resolucao do sistema ####################
  

  # ############## resultados ##################
  print('Vetor X:')
  utils.printVector(x)
  if idet > 0:
    print('Determinante:')
    print(det)
    print()
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
