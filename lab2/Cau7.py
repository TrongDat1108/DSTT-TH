import numpy as np

x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])

# cau a
print("Cau A: ", max(x))

# cau b
print("Cau B: ", min(x))

# cau c
def cauC():
    for i in range(0, len(x)):
        if x[i] >= 10:
            print("The index of the values of x that are greater than 10: %d" % (i))
cauC()

# cau d
print("Cau D: ", x[::-1])

# cau e
print("Cau E: ", np.sort(x))

# cau f
print("Cau F: ", -np.sort(-x))

# cau g
def cauG():
    count = 0
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if i != j and (x[i]+x[j]) == 0:
                count += 1
    return count
print("Cau G: ", cauG())

# cau h
# def cauH():
#     result = 0
#     for i in range(0, len(x)):
#         for j in range(i+1, len(x)):
#             if x[i] == x[j]:
#                 result += 1
#     return result
# print("Cau H: ", cauH())
# print("Cau H: ", len(x) - len(set(x)))
a = list(x)
sol7 = {i:a.count(i) for i in a if (a.count(i) >= 2)}
print("Cau H: ", len(sol7))

# cau i
def cauI():
    list = []
    for i in range(0, len(x)):
        y = x[i] + x[len(x)-i-1]
        list.append(y)
    return np.array(list)
print("Cau I: ", cauI())

# cau j
def cauJ():
    def checkAmstrong(x):
        count = result = 0
        temp = x
        while x > 0:
            x = int(x / 10)
            count += 1
        while temp > 0:
            result += (temp % 10)**count
            temp = int(temp /10)
        return result
    w = []
    for i in range(0, len(x)):
        if checkAmstrong(x[i]) == x[i]:
            w.append(x[i])
    return np.array(w)
print("Cau J: ", cauJ())

# cau k
def cauK():
    k = []
    for i in x:
        if i >= 0:
            k.append(i)
    return np.array(k)
print("Cau K: ", cauK())

# cau l
def cauL():
    temp = 0
    l = np.sort(x)
    if len(x) % 2 == 1:
        temp = l[int(len(x)/2)]
    elif len(x) % 2 == 0:
        temp = (l[int(len(x)/2-1)]+l[(int(len(x)/2))])/2
    return temp
print("Cau L: ", cauL())

# cau m
def cauM():
    m = 0
    dtb = sum(x)/len(x)
    for i in x:
        if i < dtb:
            m = m + i
    return m
print("Cau M: ", cauM())

# cau n
def cauN():
    for i in range(0,len(x)):
        if x[i] < 0:
            x[i] = -x[i]
    return x
print("Cau N: ", cauN())