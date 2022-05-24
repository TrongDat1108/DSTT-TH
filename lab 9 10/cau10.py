import numpy as np
import matplotlib.pyplot as plt
import math as m
def PlotLine(P1,P2):
    x, y = [P1[0], P2[0]], [P1[1], P2[1]]
    plt.plot(x, y, marker = 'o')
    
A = np.array([[1,1],[3,1],[1,3]])
PlotLine(A[0],A[1])
PlotLine(A[1],A[2])
PlotLine(A[2],A[0])
I3 = np.eye(3)
IA1 = -(np.dot(I3,A))

PlotLine(IA1[0],IA1[1])
PlotLine(IA1[1],IA1[2])
PlotLine(IA1[2],IA1[0])