def DiseaseSpread(P=0, N=1, R=1):
  start = N
  i = 0
  while N < P:
    if R == 1:
      if i > 0:
        N += start
    else:
      N += (R**i)*R
    i += 1
  return i
