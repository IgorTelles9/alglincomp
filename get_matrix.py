def getMatrix(file):
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
  return matrix

