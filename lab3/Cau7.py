import numpy as np

A = np.array([[2, 7, 9, 7],[3, 1, 5, 6],[8, 1, 2, 5]])

#cau a
x1 = A[:,::2]
x = x1.reshape(1,np.size(x1))
print(sum(x))

#cau b
x2 = A[::2, :]
b = x2.reshape(1,np.size(x2))
print(sum(b))

#cau c
print(A.T)