import math
import numpy as np
from matplotlib import pyplot as plt

x0 = 0
y0 = 6
xf = 15
delta = (xf-x0)/(n-1)
x = np.linspace(x0,xf,n)
py = np.zeros([n])
def f(x,y):
	return -1.335 *(y - 25)

y = np.zeros([n])
y[0] = y0

for i in range(n):
	y[i] = delta*f(x[i-1],y0) + y0
	y0 = y[i]


plt.plot(x,y,'o')
plt.xlabel("x")
plt.ylabel("y")
