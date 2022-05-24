import numpy as np

A = np.array([2, 4, 1, 6, 7, 2, 3, 5, 9]).reshape(3, 3)

print("Is A matrix square or not?", A.shape[0] == A.shape[1])
print("Is A matrix symmetric or not?", np.allclose(A, A.T))
print("Is A matrix skew-symmetric or not?", np.allclose(A, -A.T))

# Find Upper triangular matrix of A. tam giac tren
print(np.tril(A))

# Find Lower triangular matrix of A.
print(np.triu(A))