def getTriangular(m, n):
  det = 1
  for i in range(n):
    for j in range(n):
      if i  == j:
        det *= m[i][j]
  return det 