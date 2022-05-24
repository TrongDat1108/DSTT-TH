import numpy as np

#cau a
B1 = np.array([[1, -7], [-2, -3]])
print("B1:", max(np.sum(abs(B1), axis=1)))

#cau b
B2 = np.array([[3, 6], [1, 0]])
print("B2:", max(np.sum(abs(B2), axis=1)))

#cau c
B3 = np.array([[5, -4, 2], [1, 2, 3], [-2, 1, 0]])
print("B3:", max(np.sum(abs(B3), axis=1)))

#cau d
B4 = np.array([[3, 6, -1], [3, 1, 0], [2, 4, -7]])
print("B4:", max(np.sum(abs(B4), axis=1)))

#cau e
B5 = np.array([[-3, 0, 0], [0, 4 , 0], [0, 0, 2]])
print("B5:", max(np.sum(abs(B5), axis=1)))
