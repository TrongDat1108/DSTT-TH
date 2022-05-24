import sympy as sp
import numpy as np

A = sp.Matrix(np.array([[1, 0, 2, 3],
              [4, -1, 0, 2],
              [0, -1, -8, -10]]))

A2 = np.array([[1, 0, 2, 3],
              [4, -1, 0, 2],
              [0, -1, -8, -10]])

v1 = np.array(sp.Matrix.nullspace(A))[0,:].T[0]
v2 = np.array(sp.Matrix.nullspace(A))[1,:].T[0]

def is_linear_combination(A, B):
    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B)

print(v1)
print(v2)
