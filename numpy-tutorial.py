import numpy as np

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A)
print(B)

A * B  # element-wise product

A @ B  # matrix product

A.dot(B)  # another matrix product

np.ones((3, 4), dtype=float)

np.arange(12)

b = np.arange(12).reshape((3, 4))
print(b)

b.sum(axis=0)  # sum of each column

b.min(axis=1)  # min of each row


