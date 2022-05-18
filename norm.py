def euclidian(v: list, tolm: int = 1):
    ''' 
    Calcula a norma euclidiana do vetor @param v, 
    realizando arredondamento para @param tolm casas decimais. 
    '''
    norm_sqr = 0
    for element in v:
        norm_sqr += (element ** 2)
    return round((norm_sqr ** (1/2)), tolm)
