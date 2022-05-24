import numpy as np
from sympy import fibonacci
import math

def cauA():
    n = input("Enter n: ")
    a = np.arange(12, int(n), 2)
    return a
print("Cau A: b = ", cauA())

def cauB():
    n = input("Enter n: ")
    b = np.arange(31, int(n), 2)
    return b
print("Cau B: c = ", cauB())

def cauC():
    n = input("Enter n: ")
    c = np.arange(-5, int(n), 1)
    return c
print("Cau C: x = ", cauC())

def cauD():
    n = input("Enter n: ")
    d=np.arange(5,int(n),-1)
    return d
print("Cau D: y = ", cauD())

def cauE():    
    n = input("Enter n: ")
    e=np.arange(10,int(n),-2)
    return e
print("Cau E: z = ", cauE())

def cauF():    
    n = input("Enter n: ")
    f=1/(2**np.arange(int(n)))
    return f
print("Cau F: w = ", cauF())

def cauG():
    n = int(input("Enter n: "))
    caug = np.array([])
    for i in range(1,n+1):
        caug = np.append(caug,1/fibonacci(i))
    return caug
print("Cau G: d = ", cauG())

def cauH():
    n = int(input("Enter n: "))
    h = [2]
    i = 3
    while len(h) != n:
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            h.append(i)
        i = i + 2

    for i in range(len(h)):
        h[i] = 1/h[i]
    return h
print("Cau H: e = ", cauH())


def cauI(): 
    n = input("Enter n: ")
    i = []
    temp = 0
    for j in range(int(n)):
        temp = temp + j + 1
        i.append(temp)
    return i
print("Cau I: a = ",cauI())

def cauJ():
    n = int(input("Enter n: "))
    j = []
    temp  = 2
    for i in range(0, n + 1):
        if i%2== 1 and i!= 1 or i == 0:
            temp = (temp + i)
            j.append(1/temp)
    index = np.array(j)
    return index
print("Cau J: n = ", cauJ())

def cauK():
    n = int(input("Enter n: "))
    k = np.array([])
    for i in range(0, n):
        k = np.append(k, i/(i+1))
    return k 
print("Cau K: p = ", cauK())

def cauL():
    n = int(input("Enter n: "))
    l = np.array([])
    if n > 0 and n <= 25:
        for i in range(97, 97+n+1):
            l = np.append(l, chr(i))
    return l
print("Cau L: o = ", cauL())

def cauK():
    n = int(input("Enter n: "))
    m = np.array([])
    if n > 0 and n <= 25:
        for i in range(65, 65+n+1, 3):
            m = np.append(m, chr(i))
    return m
print("Cau K: m = ", cauK())