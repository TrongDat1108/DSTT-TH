from fractions import Fraction
import numpy as np

def get_hilbert_matrix(n):
    res = np.zeros((n,n), dtype=Fraction)
    for i in range(n):
        for j in range(n):
            res[i,j] = Fraction(1 , (i + j + 2 - 1))
    return res

a = get_hilbert_matrix(5)

for i in range(5):
    for j in range(5):
        print(a[i,j], end=' ')
    print()
