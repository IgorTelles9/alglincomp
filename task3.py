import determinant
import wr_utils
import eigen 

loop = True 

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE REGRESSÃO E INTERPOLAÇÃO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa calcula o valor aproximado de uma função utilizando os seguintes métodos:')
print()

wr_utils.displayMethodOptions(2)

while loop:
  (ordem, icod, idet, arquivo_a, tolm) = wr_utils.config(3)

  matriz = wr_utils.getMatrix(arquivo_a)
  #itCounter = 0

 
  

  # ############## resultados ##################
 
  
  # ############## fim resultados ##################
  
  again = input('Gostaria de resolver outro sistema? (s para sim) ')
  if again != 's':
    loop = False 
    
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
