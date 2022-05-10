def printMatrix(matrix):
  m = ''
  for line in matrix: 
    m += str(line) + '\n'
  print(m)

def printVector(vector):
  v = ''
  for number in vector:
    v += '[%s]\n' %(number)
  print(v)
  
def displayMetodos():
    print('Decomposicao LU (ICOD=1)')
    print('Decomposicao de Cholesky (ICOD=2)')
    print('Procedimento Iterativo Jacobi (ICOD=3)')
    print('Procedimento Iterativo Gauss-Seidel (ICOD=4)')
    print()

def displayDeterminante():
    print('Nao calcular determinante (IDET = 0)')
    print('Calcular determinante (IDET > 0)')
    print()
    


def configura():
    ordem = int(input('Ordem do sistema de equacoes: '))
    print()
    icod = int(input('ICOD relativo ao metodo de analise (para exibir novamente a lista de metodos, digite 0): '))
    print()
    if icod == 0:
      displayMetodos()
      icod = int(input('ICOD relativo ao metodo de analise: '))
    
    idet = 0
    if icod == 1 or icod == 2:
      displayDeterminante()
      idet = int(input('IDET relativo ao determinante: '))
      print()
    else:
      print('o metodo escolhido nao calcula determinante')
      print()
    
    arquivo_a = input('Nome do arquivo que contem a matriz A: ')
    print()
    arquivo_b = input('Nome do arquivo que contem o vetor B: ')
    print()
    
    tolm = 0
    if icod == 3 or icod == 4:
      tolm = int(input('Tolerancia maxima para solucao iterativa (1 = 10^-1; 2 = 10^-2, etc): '))
      print()
    
    return ordem,icod,idet, arquivo_a, arquivo_b, tolm 

def getMatrix(file, vector=False):
  '''
    Converte um arquivo de texto que contém uma matriz em uma lista python.
    
    Formato esperado para o arquivo: 
      cada linha da matriz ocupando uma linha no arquivo,
      separação entre números utilizando um espaço ' '. 
  '''
  with open(file) as reader:
    line = reader.readline()
    matrix = []
    while line != '':
      if (line.find('\n') != -1):
        line = line.replace('\n', '')
      line = line.split(' ')
      float_line = []
      for item in line:
        float_line.append(float(item))
      matrix.append(float_line)
      line = reader.readline()
  if len(matrix) == 1:
    return matrix[0]
  return matrix

