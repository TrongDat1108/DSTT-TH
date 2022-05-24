import numpy as np

def find_proj(y, u):
    res = (sum(y*u)/sum(u*u)) * u
    return res

x = np.array([[-10, 13, 7, -11],
              [2, 1, -5, 3],
              [-6, 3, 13, -3],
              [16, -16, -2, 5],
              [2, 1, -5, -7]])

v = np.zeros((x.shape))
v[:,0] = x[:,0]


for i in range(1, len(x[0])):
    temp = x[:,i]
    for j in range(i):
        temp = temp - find_proj(x[:,i], v[:,j])
    v[:,i] = temp

print(v)