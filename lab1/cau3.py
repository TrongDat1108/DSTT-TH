import numpy as np
d = {1:'banana', 2:'monkey', 3:'apple', 4:'dog', 5:'cat', 6:'tiger', 7:'cows', 8:'banana', 9:'watermelon', 10:'apple'}
d1 = d.copy()
#cau a5
count = 0
x = input('Enter x: ')

for i in d.keys():
    if x == d[i]:
        count = count + 1
print(str(x) + " xuat hien "+str(count)+" lan.")

#cau b
k = input("Enter k: ")
for i in d1.keys():
    if x == d1[i]:
        d1[i] = k
print(d1)

#cau c
ip = x
for i in range (1, len(d.keys())+1):
    if ip == d[i]:
        d1.pop(i)
print(d1)

#cau d
d[10] = x
print(d)