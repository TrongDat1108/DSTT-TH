from posixpath import split
import numpy as np
def split_message(string):
    res = []
    res[:0]= string
    return res
A = np.array([[3, 4, 5],[1, 3, 1], [1, 1, 2]])
lookupTable = list(map(chr, range(65, 91)))
lookupTable.append(" ")
# lookupTable.append("")
print(lookupTable)
for i in range(len(lookupTable)):
    print("{}-{}".format(i, lookupTable[i]),end="")
    print("---")
message1 = "ATTACK"
message2 = "LINEAR ALGEBRA LABORATORY"
split_message1 = split_message(message1)
split_message2 = split_message(message2)
# print(split_message1)
# print(split_message2)
# first_line = []
# for i in range(len(split_message1)):
#     for j in range(len(lookupTable)):
#         if split_message1[i] == lookupTable[j]:
#             first_line.append(j)
# E = np.array(first_line)+4
# E = E.reshape(int(len(E)/3),3).T
# print(A@E)
def encodeMessage(list_char, A, lookupTable):
    first_line = []
    for i in range(len(list_char)):
        for j in range(len(lookupTable)):
            if list_char[i] == lookupTable[j]:
                first_line.append(j)
                if list_char[i] == " ":
                    first_line.append(j)
                break
    print(first_line)
    E = np.array(first_line)+4
    print(E)
    # print(len(E))
    E = E.reshape(int(len(E)/3),3).T
    # E = E.reshape(int(len(E)/5),3).T

    # print(int(len(E)/5))
    # E = E.reshape(int(len(E)/5),3)

    # print(E)
    
    return A@E
# print(encodeMessage(split_message1, A, lookupTable))
print(encodeMessage(split_message2, A, lookupTable))
