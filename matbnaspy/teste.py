import numpy as np
import pylab as pl

def f(x):
  if (x<0):
    return -1
  elif (x>0):
    return 1

if __name__ == "__main__":
  n = 1000
  x = np.linspace(-10,10,n)
  y = np.zeros(n)

  for i in range(0,n,1):
    y[i] = f(x[i])

  pl.plot(x,y)
  pl.show()
