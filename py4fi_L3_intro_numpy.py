import numpy as np

'''
N-dimensional array
'''

# Array creation

a = np.array([1,2,3,4])

b = np.array([(1.5,2,3), (4,5,6)])
b.dtype
np.zeros((3,4))

np.ones((2,3,4))

np.arange( 10, 30, 5 )
np.arange( 0, 2, 0.3 )                 # it accepts float arguments

from numpy import pi
x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points

c = np.arange(24).reshape(2,3,4)         # 3d array


# Basic operations

a = np.arange(10)
b = 4*a
a *= 4
b-a == 3*a
a**2
np.sin(a)
np.exp(a)
np.sqrt(a)

A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0], [3,4]] )
A*B                         # elementwise product
A.dot(B)                    # matrix product
np.dot(A, B)                # another matrix product

a = np.random.random((2,3))
a.sum(), a.min(), a.max()

b = np.arange(12).reshape(3,4)
b.cumsum(axis=1)                         # cumulative sum along each row
np.mean(b)
np.mean(b, axis=0)

