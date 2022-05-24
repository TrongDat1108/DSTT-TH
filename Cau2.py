import numpy as np
import matplotlib.pyplot as plt

a1 = 1
a2 = 2
b1 = 2
b2 = 4
c1 = 50
c2 = 1

x = np.arange(-10, 50)

y1 = (c1 - a1*x)/b1
y2 = (c2 - a2*x)/b2

fig = plt.figure()
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'b')
plt.show()
