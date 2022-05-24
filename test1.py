import numpy as np


A = np.array([[1, 3, 4, 5],
              [2, 2, 4, 3],
              [-1, 1 ,3, -6],
              [0, -4, -3, 5]])

def req1(A):
    temp = list()
    for i in A:
        temp.append(sum(i))
    maximum = max(temp)
    result = list()
    for j in A:
        if sum(j) == maximum:    
            result.append(j)
    return result
print(req1(A))

def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;

def req2(A):
    result = 0
    for i in range(0, len(A)):
        # for j in range(i):
        result = result + fibonacci(A[i][i])
    return result
print(req2(A))