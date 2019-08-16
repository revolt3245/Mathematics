import numpy as np

base = 15
len1 = 11
len2 = 13

point = np.zeros(2)

point[0] = (len1**2 - len2**2 + base**2)/(2*base)
point[1] = np.sqrt(len1**2 - point[0]**2)