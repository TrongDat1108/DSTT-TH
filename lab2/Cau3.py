import numpy as np

n = int(input("Enter n: "))

c = []

for i in range(1, n + 1):
    c.append(pow(10, i))
print(np.array(c))
