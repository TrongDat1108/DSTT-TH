import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a1 = 1 
a2 = 2 
b1 = 2
b2 = 4 
c1 = 3
c2 = 6
d1 = 50
d2 = 500

x, y = np.meshgrid(np.arange(-5, 5), np.arange(-5, 5))

z1 = (d1 - a1*x - b1*y)/c1 
z2 = (d2 - a2*x - b2*y)/c2 

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y , z1, cmap = plt.cm.ocean, alpha = 0.4)
ax.plot_surface(x, y , z2, cmap = plt.cm.cool, alpha = 0.7)
plt.show()