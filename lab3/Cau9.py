import numpy as np

T = np.array([[0.6, 0.7],[0.4, 0.3]])
p = np.array([[0.5],[0.5]])
k = int(input())
for i in range(k+1):
    T = T.dot(T)
pk = T.dot(p)
print(pk)