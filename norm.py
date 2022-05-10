def euclidian(v:list, tolm:int=1):
  norm_sqr = 0
  for element in v:
    norm_sqr += (element ** 2)
  return round((norm_sqr ** (1/2)),tolm)