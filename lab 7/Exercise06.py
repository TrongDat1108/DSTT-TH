import numpy as np

def is_linear_combination(A, B):
    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B)

def cauA():
    v1 = np.array([1, 2, 3, 4])
    v2 = np.array([-1, 0, 1, 3])
    v3 = np.array([0, 5, -6, 8])
    w = np.array([3, -6, 17, 11])
    print(f"a) {is_linear_combination([v1, v2, v3], [v1, v2, v3, w])}")

def cauB():
    v1 = np.array([1, 1, 2, 2])
    v2 = np.array([2, 3, 5, 6])
    v3 = np.array([2, -1, 3, 6])
    w = np.array([0, 5, 3, 0])
    print(f"b) {is_linear_combination([v1, v2, v3], [v1, v2, v3, w])}")

def cauC():
    v1 = np.array([1, 1, 2, 2])
    v2 = np.array([2, 3, 5, 6])
    v3 = np.array([2, -1, 3, 6])
    w = np.array([-1, 6, 1, -4])
    print(f"c) {is_linear_combination([v1, v2, v3], [v1, v2, v3, w])}")

def cauD():
    v1 = np.array([1, 2, 3, 4])
    v2 = np.array([-1, 0, 1, 3])
    v3 = np.array([0, 5, -6, 8])
    v4 = np.array([1, 15, -12, 8])
    w = np.array([0, -6, 17, 11])
    print(f"d) {is_linear_combination([v1, v2, v3, v4], [v1, v2, v3, v4, w])}")

cauA()
cauB()
cauC()
cauD()