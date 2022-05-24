import numpy as np

def find_cos_sim(a,b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

d1 = np.array([0,4,0,0,0,2,1,3])
d2 = np.array([3,1,4,3,1,2,0,1])
d3 = np.array([3,0,0,0,3,0,3,0])
d4 = np.array([0,1,0,3,0,0,2,0])
d5 = np.array([2,2,2,3,1,4,0,2])

arr = [d1, d2, d3, d4, d5]

for i in range(len(arr) - 1):
    for j in range(i + 1,len(arr)):
        print(f"Doc{i + 1} & Doc{j+1} = {find_cos_sim(arr[i], arr[j])}")