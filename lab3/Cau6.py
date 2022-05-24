import numpy as np

A = np.array([[2, 4, 1],[6, 7, 2], [3, 5, 9]])

#cau a
x1 = A[0,:]
print(x1)

#cau b
x2 = A[-2:,:]
print(x2)