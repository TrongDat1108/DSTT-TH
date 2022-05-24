import numpy as np

A = np.array([[2, 2], [2, 3]])
B = np.array([4, 6])

x = np.linalg.inv(A.T@A)@A.T@B.T
print(x)