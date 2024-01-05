# a = np.arange(15).reshape(3, 5)
import numpy as np
a=np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
rray=([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

a1=rray.__len__()
l1=[1,2,3]
n=rray.__add__(l1)
print(a1)
print(n)
print(a+rray)
