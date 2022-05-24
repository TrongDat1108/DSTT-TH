import numpy as np

def find_cos_sim(a,b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))


q = np.array([0, 0, 0.7, 0.5, 0, 0.3])
data = np.array([[1, 0.5, 0.3, 0, 0, 0],
                 [0.5, 1, 0, 0, 0, 0],
                 [0, 1, 0.8, 0.7, 0, 0],
                 [0, 0.9, 1, 0.5, 0, 0],
                 [0, 0, 0, 1.0, 0, 1.0],
                 [0, 0, 0, 0, 0.7, 0],
                 [0.5, 0, 0.7, 0, 0, 0.9],
                 [0, 0.6, 0, 1, 0.3, 0.2]])

max = find_cos_sim(q,data[0])
idx = 0

for i in range(1, len(data)):
    cos_sim = find_cos_sim(q, data[i])
    if max < cos_sim:
        max = cos_sim
        idx = i

print(f"The nearest with vector q is: D{idx+1} with cos_sim = {max}")