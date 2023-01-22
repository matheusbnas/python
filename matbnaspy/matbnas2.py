import numpy as np
import matplotlib.pyplot as pit

def f(x):
  return np.cos(x)
def g(x):
  return np.sin(x)

a= -10
b= 10
n= 1000

x=np.linspace(a, b, n)

y1=f(x)
y2=g(x)

pit.xlabel("x")
pit.ylabel("y")
pit.title("exemplo 1")

pit.grid(True)
pit.plot(x,y1)
pit.plot(x,y2)
pit.show()
