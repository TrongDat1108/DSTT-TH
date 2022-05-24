import numpy as np

A=np.array([-1,4,8,-9,1,2]).reshape(2,3)
B=np.array([5,8,0,-6,5,6]).reshape(3,2)
C=np.array([-4,1,6,5]).reshape(2,2)
D=np.array([-6,3,1,8,9,-2,6,-1,5]).reshape(3,3)

# print("Câu a: ",A.dot(B.T))

print("Câu b: ", B.dot(C.T))
print("Câu c: ", C-C.T)
print("Câu d: ", D-D.T)
print("Câu e: ",(D.T).T)
print("Câu f: ", 2*C.T)
print("Câu g: ", A.T+B)
print("Câu h: ", (A.T+B).T)
print("Câu i: ", (2*A.T-5*B).T)
print("Câu j: ", (-D).T)
print("Câu k: ", -(D.T))
print("Câu l: ", (C.dot(C)).T)
print("Câu m: ", (C.T).dot(C.T))