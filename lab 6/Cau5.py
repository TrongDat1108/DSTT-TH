import numpy as np

#cau a
u = np.array([2, 3])
un_v = u/(np.linalg.norm(u,2))
print("a)",un_v)

#cau b
ub = np.array([1, 2, 3])
un_b = ub/(np.linalg.norm(ub,2))
print("b)",un_b)

#cau c
uc = np.array([1/2, -1/2, 1/4])
un_c = uc/(np.linalg.norm(uc,2))
print("c)",un_c)

#cau d
ud = np.array([np.sqrt(2), 2, -np.sqrt(2), np.sqrt(2)])
un_d = ud/(np.linalg.norm(ud,2))
print("d)",un_d)