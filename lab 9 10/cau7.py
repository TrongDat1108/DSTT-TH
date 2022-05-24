import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt

#cau7
def Sxy(p,l,m):
  S = np.array([[1,0],[0,m]])
  Sp = S.dot(p)
  return Sp

p1 = np.array([1,1])
p2 = np.array([-1,1])
p3 = np.array([-1,-1])
p4 = np.array([1,-1])

#caua:
l = m = 2
q1 = Sxy(p4,l,m)
q2= Sxy(p2,l,m)
q3 = Sxy(p3,l,m)
q4 = Sxy(p4,l,m)
print(p1, "=>", q1)
print(p2, "=>", q2)
print(p3, "=>", q3)
print(p4, "=>", q4)

#Cau b:
l = m = 0.5
q1 = Sxy(p4,l,m)
q2= Sxy(p2,l,m)
q3 = Sxy(p3,l,m)
q4 = Sxy(p4,l,m)
print(p1, "=>", q1)
print(p2, "=>", q2)
print(p3, "=>", q3)
print(p4, "=>", q4)

#cauc:
l = 1
m = -1
q1 = Sxy(p4,l,m)
q2= Sxy(p2,l,m)
q3 = Sxy(p3,l,m)
q4 = Sxy(p4,l,m)
print(p1, "=>", q1)
print(p2, "=>", q2)
print(p3, "=>", q3)
print(p4, "=>", q4)

#caud:
l = -1
m = 1
q1 = Sxy(p4,l,m)
q2= Sxy(p2,l,m)
q3 = Sxy(p3,l,m)
q4 = Sxy(p4,l,m)
print(p1, "=>", q1)
print(p2, "=>", q2)
print(p3, "=>", q3)
print(p4, "=>", q4)
