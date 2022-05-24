import  numpy as np

#cau a
ls1 = [0, 2, 4, 6 , 8]

t = tuple(ls1)
print(t)

#cau b

s = set(ls1)
print(s)

#cau c

d = dict()
for i, v in enumerate(ls1):
    d[i] = v
    
print(d)