import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A[[0,2],:]=A[[2,0],:]
print(A)
