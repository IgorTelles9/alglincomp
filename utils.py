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