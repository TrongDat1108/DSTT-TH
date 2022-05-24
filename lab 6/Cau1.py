import numpy as np

#cau a
A1 = np.array([[1, -7], [-2, -3]])

print("A1:", max(np.sum(abs(A1), axis = 0)))

#cau b
A2 = np.array([[-2, 8], [3, 1]])
print("A2:", max(np.sum(abs(A2), axis = 0)))

#cau c
A3 = np.array([[2, -8], [3, 1]])
print("A3:", max(np.sum(abs(A3), axis = 0)))

#cau d
A4 = np.array([[2, 3], [1, -1]])
print("A4:", max(np.sum(abs(A4), axis = 0)))

#cau e
A5 = np.array([[5, -4, 2], [-1, 2, 3], [-2, 1, 0]])
print("A5:", max(np.sum(abs(A5), axis = 0)))
