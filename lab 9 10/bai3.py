import numpy as np
from sympy import *

M=np.array([[-3,-5,-7],
            [-2,1,0],
            [1,5,5]])
values,vectors=np.linalg.eig(M)

x,y,z=symbols('x,y,z')
for k in values:
    m=M-k*np.eye(3) 
    print("the solution of the equation",np.linalg.solve(m,[0,0,0]))
P=vectors.T
D=np.linalg.inv(P)@M@P
print("cau3 lap 10")
print(D)
print(M)
