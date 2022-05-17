import eigen

#matrix = [ [1.0, 0.2, 0.0], [0.2,1.0,0.5], [0.0,0.5,1.0] ]
matrix = [[5, -4, 1, 0], [-4, 6, -4, 1], [1, -4, 6, -4], [0, 1, -4, 5]]
order = 4

values, vectors, counter = eigen.jacobi(matrix, order,2)
print(values)
print(vectors)