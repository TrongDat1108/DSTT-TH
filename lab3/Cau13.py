import numpy as np
import random
A=np.random.randint(1,10,size=(5,5))
B=np.random.randint(1,10,size=(5,5))
res_A=np.linalg.det(A+B)
res_B=np.linalg.det(A)+np.linalg.det(B)
print(res_A)
print(res_B)


for _ in range(3):
  n=random.randint(2,5)
  A=np.random.randint(1,10,size=(n,n))
  B=np.random.randint(1,10,size=(n,n))
  print(A)
  print(B)
  res_A=np.linalg.det(A+B)
  res_B=np.linalg.det(A)+np.linalg.det(B)
  print("det(A)=",res_A)
  print("det(B)=",res_B)
  if round(res_A)!=round(res_B):
    print('wrong')
  else:
    print('correct')