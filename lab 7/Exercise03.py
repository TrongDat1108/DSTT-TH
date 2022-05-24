import numpy as np

m = np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])

def check_orthonormal(matrix):
    if (matrix.shape[0] == matrix.shape[1]):
        if np.array_equal(matrix.T * matrix , np.eye(matrix.shape[0])):
            return True
        else:
            return False
    else:
        return False

print(check_orthonormal(m))


