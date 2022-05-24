import numpy as np

u1 = np.array([3,1,1])
u2 = np.array([-1,2,1])
u3 = np.array([-1/2,2,7/2])

data = [u1,u2,u3]

for i in range(len(data)-1):
    for j in range(i + 1, len(data)):
        res = sum(data[i] * data[j])
        if res == 0:
            print(f"u{i+1} and u{j+1} are orthogonal set")
        else:
            print(f"u{i+1} and u{j+1} are not orthogonal set")