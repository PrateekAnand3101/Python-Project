
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

#x = [24,25,26]
#y = [23,24,25]
#plt.plot(x,y)
#plt.show()
x = np.linspace(0, 10,1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()
plt.scatter(x[::10], y[::10], color = 'green')
plt.show()
