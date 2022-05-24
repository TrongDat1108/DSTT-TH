import numpy as np
s1 = np.array([1, 2, 3]).T
s2 = np.array([7, 4, 3]).T
s3 = np.array([2, 1, 9]).T
dis_s1_s2 = np.linalg.norm(s2-s1)
dis_s1_s3 = np.linalg.norm(s3 - s1)
dis_s2_s3 = np.linalg.norm(s3- s2)
print(dis_s1_s2)
print(dis_s1_s3)
print(dis_s2_s3)