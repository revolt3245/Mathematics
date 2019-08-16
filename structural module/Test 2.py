import numpy as np
import numpy.linalg as lin

dot1 = np.array([7., 5.])
dot2 = np.array([15., 19.])

print(lin.norm(dot1 - dot2))
len1 = 15
len2 = 19

dot3 = np.random.rand(2)

def Grad(dot1, dot2, dot3, l1, l2):
    reg = 2*l1/lin.norm(dot3 - dot1) + 2*l2/lin.norm(dot3-dot2)
    return (2-reg)*dot3 - dot1 - dot2

def Hessian(dot1, dot2, dot3, l1, l2):
    Hessian1 = np.eye(2)
    dot3_1 = dot3.reshape(-1,1)
    Hessian2 = np.matmul(dot3_1, dot3_1.T)
    return Hessian1*2*(1-len1/lin.norm(dot3 - dot1) -len2/lin.norm(dot3-dot2)) + 2*Hessian2*(len1/(lin.norm(dot3-dot1)**3)+len2/(lin.norm(dot3-dot2)**3))

for i in range(1000):
    Gradient = Grad(dot1, dot2, dot3, len1, len2)
    Hess = Hessian(dot1, dot2, dot3, len1, len2)
    Hessinv = lin.inv(Hess)
    dot3 -= np.matmul(Hessinv, Gradient)