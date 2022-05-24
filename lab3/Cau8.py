import numpy as np

A = np.array([[12, 15, 10, 16, 12],[5, 9, 14, 7, 10],[8, 12, 10, 9, 15]])
B = np.array([[2, 1, 3]])
D = B.dot(A)
print(sum(D))