import numpy as np

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

#cau a
print("Cau A: ", x[0:6:1])

#cau b
print("Cau B: ", x[-5::])

#cau c
print("Cau C: ", np.array([x[0], x[3], x[-1]]))

#cau d
print("Cau D: ", np.array([x[0], x[2], x[4], x[6]]))

#cau e
# def cauE():
#     e = []
#     for i in x:
#         if i % 2 != 0:
#             e.append(i)
#     return e
# print("Cau E: ", cauE())
print("Cau E: ", x[1::2])

#cau f
# def cauF():
#     f = []
#     for i in x:
#         if i % 2 == 0:
#             f.append(i)
# #     return np.array(f)
# print("Cau F: ", cauF())
print("Cau F: ", x[::2])