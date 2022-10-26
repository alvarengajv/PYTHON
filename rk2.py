import math
import numpy as np
from matplotlib import pyplot as plt

x0 = 0
y0 = 6
xf = 15
n = 10
deltax = (xf-x0)/(n-1)
x = np.linspace(x0,xf,n)
def f(x,y):
	return -1.335 *(y - 25)
y = np.zeros([n])
y[0] = y0
py = np.zeros([n])
py[0] = None

for i in range(1,n):
	py[i] = deltax*f(x[i-1],y[i-1]) + y[i-1]
	y[i] = deltax/2*( f(x[i],py[i]) + f(x[i-1],y[i-1]) ) + y[i-1]
print("x_n\t    y_n")
for i in range(n):
	print(x[i],"\t",format(y[i],'6f'))
plt.plot(x,y,'o')
plt.xlabel("x")
plt.ylabel("y")

plt.show()
