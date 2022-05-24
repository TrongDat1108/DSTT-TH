import numpy as np
import matplotlib.pyplot as plt
import math as m
v1 = np.array([ [3],[3] ])
R1 = np.array([ [-1,0],
               [0,-1] ])
n1 = R1.dot(v1)
print("a) ",n1)
##
v2 = np.array([ [3],[3] ])
R2 = np.array([ [1/2,-(m.sqrt(3)/2)],
               [m.sqrt(3)/2,1/2] ])
n2 = R2.dot(v2)
print("b) ",n2)