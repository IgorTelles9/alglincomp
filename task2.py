import determinant
import wr_utils
import eigen 

loop = True 

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE AUTOVALORES E AUTOVETORES')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa calcula autovalores e autovetores utilizando os seguintes métodos:')
print()

wr_utils.displayMethodOptions(2)

while loop:
  (ordem, icod, idet, arquivo_a, tolm) = wr_utils.config(2)

  matriz = wr_utils.getMatrix(arquivo_a)
  det = 0
  itCounter = 0

  # ############### calculo de autovetores e autovalores ####################
  if icod == 1:
    pass
    
  if icod == 2: 
    # ############ metodo de jacobi ###############
    (autovalores, autovetores, itCounter) = eigen.jacobi(matriz,ordem,tolm)
    autovalores_list = [autovalores[i][i] for i in range(ordem)]
    
    # calculo de determinante
    if idet > 0:
      det = determinant.getTriangular(autovalores,ordem)
    # fim calculo de determinante
    # ############ fim metodo de jacobi ############### 
  
  # ############### fim calculo de autovetores e autovalores ####################
  

  # ############## resultados ##################
  if icod == 1:
    print('Maior autovalor: ')
    print()
    print()
    
    print('Autovetor associado: ')
    wr_utils.printVector()
    print()
    
  if icod == 2: 
    print('Autovalores: ')
    wr_utils.printVector(autovalores_list)
    print()
    
    print('Matriz de Autovetores: ')
    wr_utils.printMatrix(autovetores)
    print()
  
    if idet > 0:
      print('Determinante:')
      print(det)
      print()
    
  print('Numero de iteracoes: %s'  % (itCounter))
  print()
  
  # ############## fim resultados ##################
  
  again = input('Gostaria de resolver outro sistema? (s para sim) ')
  if again != 's':
    loop = False 
    
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
