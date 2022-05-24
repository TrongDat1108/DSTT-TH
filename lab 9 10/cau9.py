import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt

#cau9
def PlotLine(P1,P2):
    x, y = [P1[0], P2[0]], [P1[1], P2[1]]
    plt.plot(x, y, marker = 'o')

A = np.array([0,2])
B = np.array([1,3])
C = np.array([5,3])
D = np.array([6,2])
E = np.array([5,2])
F = np.array([5,0])
G = np.array([1,0])
H = np.array([1,2])
I = np.array([0,2])

PlotLine(A,B)
PlotLine(B,C)
PlotLine(C,D)
PlotLine(D,E)
PlotLine(E,F)
PlotLine(F,G)
PlotLine(G,H)
PlotLine(H,A)