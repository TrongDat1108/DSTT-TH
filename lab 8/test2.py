import numpy as np
import matplotlib.pyplot as plt

#w = w0 + w1x1 + w2x2 + w3x3
X = np.array([[1, 60, 5.5, 1],
            [1, 65, 5, 0],
            [1, 55, 6, 1],
            [1, 50, 5, 1]])

Y = np.array([66, 74, 78, 72])

w = np.linalg.inv(X.T@X)@X.T@Y.T

print(w)

we = 60
he = 5
sm = 1

y_p = w[0] + w[1]*we + w[2]*he + w[3]*sm
print(y_p)