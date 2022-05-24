import numpy as np

def angleBetweenTwoVector(a, b):
    res = (np.dot(a/np.linalg.norm(a), b/np.linalg.norm(b)))
    return res

u1 = np.array([1, 1])
v1 = np.array([0, 1])
print(angleBetweenTwoVector(u1, v1))
u2 = np.array([1, 0])
v2 = np.array([0, 1])
print(angleBetweenTwoVector(u2, v2))
u3 = np.array([-3, 3])
v3 = np.array([1/2, -1/2])
print(angleBetweenTwoVector(u3, v3))