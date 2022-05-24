
import numpy as np
from numpy import *

A = np.array([[1, 2, 16, 31, 22],[2, 8, 12, 21, 23], [4, 9, 11, 14, 25], 
[3, 6, 10, 16, 34]])
#Câu a
B = A[1:2,1:4]
print(B)
#Câu b
C = A[1:3,1:4]
print(C)
#câu c
D = A[:, 2].reshape(4,1)
print(D)
#Câu d
E = A[:, ::2]
print(E)
#Câu E
F = A[1:4, [0,2,3,4]]
print(F)
#Câu F
G = np.where(A<12, 0 , A)
G = delete(np.where(A==0))
print(G)