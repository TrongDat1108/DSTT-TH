import numpy as np

#cau a
A = np.array([[1, 0], 
              [1, 1],
              [1, 2], 
              [1, 3]])

B = np.array([1, 1, 2, 2])

y = np.linalg.inv(A.T@A)@A.T@B.T
print(y)

#cau b
def cauB():
    B = np.array([[1, 1],
                  [1, 2],
                  [1, 4],
                  [1, 5]])
    
    b = np.array([0, 1, 2, 3])
    
    y = np.linalg.inv(B.T@B)@B.T@b.T
    return y
print(cauB())

#cau c
def cauC():
    A=np.array([[1, -1],
                [1, 0],
                [1, 1],
                [1, 2]])
    b=np.array([0,1,2,4])
    
    y = np.linalg.inv(A.T@A)@A.T@b.T
    return y
print(cauC())

#cau d
def cauD():
    A=np.array([[2,1],[3,1],[5,1],[6,1]])
    b=np.array([3, 2, 1, 0])
    y = np.linalg.inv(A.T@A)@A.T@b.T
    return y
print(cauD())
    