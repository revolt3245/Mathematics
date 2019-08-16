import numpy as np
import numpy.linalg as lin

dot1 = np.array([[7.], [5.]])
dot2 = np.array([[15.], [19.]])

len1 = 15
len2 = 19

point = np.zeros((2,1))

vec = dot2 - dot1

base = lin.norm(vec)
vec /= base

point[0] = (len1**2 - len2**2 + base**2)/(2*base)
point[1] = np.sqrt(len1**2 - point[0]**2)

vec2 = np.roll(vec, 1)
vec2[0] = -vec2[0]

tensor = np.hstack([vec, vec2])

point = np.matmul(tensor, point) + dot1