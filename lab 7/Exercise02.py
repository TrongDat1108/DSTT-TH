import numpy as np

y = np.array([7,6])
u = np.array([4,2])

proju_y = (sum(y*u)/sum(u*u)) * u

print(proju_y)