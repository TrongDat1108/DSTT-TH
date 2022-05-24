import numpy as np

x = np.array([5, 6, 7, 8, 9])
y = np.arange(1,7)
c = np.arange(1,31)
d = np.arange(1,26)
A = (np.repeat(x,5, axis = 0)).reshape(5,5)
print(A)
B = (np.repeat(y,6, axis = 0)).reshape(6,6)
print(B.T)
C = c.reshape(6,5)
print(C.T)
D = d.reshape(5,5)
print(D)