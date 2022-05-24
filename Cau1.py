import numpy as np
from sympy import *

#option 1
A = np.array([[1, 1, -1], [1, -1, 2], [2, 1, 1]])
B = np.array([7, 3, 9])
root1 = np.linalg.inv(A)@B
print(root1)

#option 2 Ax = b => x = (A^-1)B
root2 = np.linalg.inv(A)@B
print(root2)

#option 3: Cramer
D = A.copy()
Dx = np.array([[7, 1, -1], [3, -1, 2], [9, 1, 1]])
Dy = np.array([[1, 7, -1], [1, 3, 2], [2, 9, 1]])
Dz = np.array([[1, 1, 7], [1, -1, 3], [2, 1, 9]])
r_x = np.linalg.det(Dx)/np.linalg.det(D)

r_y = np.linalg.det(Dy)/np.linalg.det(D)
r_z = np.linalg.det(Dz)/np.linalg.det(D)
print([r_x, r_y, r_z])

#option 4: 
M = Matrix([[1, 1, -1, 7], [1, -1, 2, 3], [2, 1, 1, 9]])
root4, pivot = M.rref()
print(root4)