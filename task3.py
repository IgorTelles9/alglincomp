import determinant
import wr_utils
import eigen 
from interpolacao import interpola
from regressao import regressao

loop = True 

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE REGRESSÃO E INTERPOLAÇÃO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa calcula o valor aproximado de uma função utilizando os seguintes métodos:')
print()

wr_utils.displayMethodOptions(3)

while loop:
  (icod, npares, xcoord, ycoord, xpred, func) = wr_utils.config(3)

# INTERPOLACAO  
  if icod == 1:
    ypred = interpola(npares, xcoord, ycoord, xpred)
# ACABOU A INTERPOLACAO


# REGRESSAO MULTILINEAR

  if icod == 2:
    ypred = regressao(npares, xcoord, ycoord, func, xpred)

# ACABOU A REGRESSAO MULTILINEAR


  # ############## resultados ##################
  print(f'A funcao avaliada no ponto {xpred} vale: {ypred}')
  
  # ############## fim resultados ##################
  
  again = input('Gostaria de resolver outro sistema? (s para sim) ')
  if again != 's':
    loop = False 
    
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
