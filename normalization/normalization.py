import numpy as np

def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

A = np.random.randn(3,3,3)
print(normalized(A,0))
# print(normalized(A,1))
# print(normalized(A,2))

# print(normalized(np.arange(3)[:,None]))
# print(normalized(np.arange(3)))