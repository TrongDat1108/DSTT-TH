import sympy
import numpy as np

A = sympy.Matrix(np.array([[1,0,2,3],
                           [4,-1,0,2],
                           [0,-1,-8,-10]]))

C,pivot = sympy.Matrix.rref(A)

C = np.array(C)

print("The basis of row space is: ")
print(np.array(C[pivot, :]))

print("The basis of column space is: ")
C,pivot = sympy.Matrix.rref(A.T)
print(np.array(A[:, pivot]))
