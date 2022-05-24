import numpy as np
from sympy import *


a1 = np.array([[1,1,1],[1,2,4],[1,3,9]])
b1 = np.array([6,15,38])
caua = np.linalg.solve(a1,b1.T)
print(caua)