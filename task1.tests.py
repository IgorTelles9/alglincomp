from lu import luDecomposition

m1 = [[5, -4, 1, 0], [-4, 6, -4, 1], [1, -4, 6, -4], [0, 1, -4, 5]]
m2 = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]

print(luDecomposition(m1, 4))