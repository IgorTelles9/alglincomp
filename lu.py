def luDecomposition(matrix: list, size: int) -> list:
    for k in range(size-1):
      # k é a coluna do pivô
        for i in range(k+1, size, 1):
          # i assume o valor de cada linha abaixo do pivô
            matrix[i][k] = round((matrix[i][k] / 
                                  matrix[k][k]), 2)
          # para economizar memória, coloca-se o item da matriz L
          # correspondente a posição que seria zerada na matriz principal

        # os loops abaixo fazem as operações nas linhas que devem ser modificadas
        for j in range(k + 1, size, 1):
            for i in range(k + 1, size, 1):
              # the operations are done in the column and line after the where the pivot is located
                matrix[i][j] = round((matrix[i][j] -
                                      (matrix[i][k] * matrix[k][j])), 2)
    return matrix
