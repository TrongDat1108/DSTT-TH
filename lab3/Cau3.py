import numpy as np

B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B[:,[2,0]]=B[:,[0,2]]
print(B)