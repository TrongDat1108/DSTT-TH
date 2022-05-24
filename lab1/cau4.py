from logging import captureWarnings
import numpy as np
S1 = {7, 8, 9, 10, 4, 5, 6, 0}
S2 = {9, 5, 2, 10, 6, 5, 8, 1, 2, 3}

#cau a
cauA = {0}
cauA.clear()
for i in S1:
    for j in S2:
        if i == j:
            cauA.add(i)
print(cauA)

#cau b
cauB = S1.copy()
for i in S2:
    cauB.add(i)
print(cauB)

#cau c
x = input('Enter x: ')
cauC = S2.copy()
cauC.update({int(x)})
print(cauC)

#cau d
x1 = input('Enter x1: ')
cauD = S1.copy()
cauD.remove(int(x1))
print(cauD)
