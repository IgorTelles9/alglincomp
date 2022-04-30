def back(upper, vector, size):
    x = size*[0.0]
    for i in range(size-1, -1, -1):
        for j in range(size-1, i-1, -1):
            if (i == j):
                x[i] = round(((vector[i] - x[i])/upper[i][i]), 2)
            else:
                x[i] += round((x[j] * upper[i][j]), 2)
    return x


def foward(lower, vector, size):
    x = size*[0.0]
    for i in range(size):
        x[i] = round((vector[i]), 2)
        for j in range(0, ((size+1+i)-size), 1):
            if (i != j):
                x[i] -= round((x[j]*lower[i][j]), 2)
                x[i] = round((x[i]), 2)
    return x
