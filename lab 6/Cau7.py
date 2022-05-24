import numpy as np
E = np.array([[80, 98, 99, 85, 106, 94], 
              [71, 92, 76, 95, 100, 92], 
              [124, 163, 140, 160, 176, 161]])
A = np.array([[1, 2, 3], 
              [2, 1, 2],
              [3, 2, 4]])
# A1 = np.linalg.inv(A)
# inv_A_E = np.dot(A1, E)
# inv_A_E_T  = inv_A_E.T
list_char = list(map(chr, range(65, 91)))
list_char.append(" ");
# inv_A_E_T = (np.round(inv_A_E_T)-4).astype(int)
def decodeMessage(a, E,list_char ):
    a = np.dot(np.linalg.inv(a),E).T
    print(a)
    a = np.round(a-4).astype(int)
    res = ""
    for i in range(len(a)):
        for j in range(len(a[0])):
            res += list_char[a[i][j]]
    return res
print(decodeMessage(A,E, list_char))