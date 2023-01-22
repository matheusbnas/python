import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.cos(x)

def g(x):
  return np.sin(x)

a = -10
b = 10
n = 1000

x = np.linspace(a, b, n)

y1 = f(x)
y2 = g(x)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Exemplo 1")

plt.grid(True)

plt.plot(x, y1, 'r')
plt.plot(x, y2, 'b')

plt.show()
