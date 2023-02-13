import numpy as np

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A)
print(B)

print(A.shape)
print(B.shape)

print(A * B)  # element-wise product

print(A @ B)  # matrix product

print(A.dot(B))  # another matrix product

print(np.ones((3, 4), dtype=float))

print(np.arange(12))

b = np.arange(12).reshape((3, 4))
print(b)

print(b.sum(axis=0))  # sum of each column

print(b.min(axis=1))  # min of each row

print(b)

print(b.T)  # returns the array, transposed

print(b.ravel())  # returns the array, flattened

print(np.vstack((b, b)))

print(np.hstack((b, b)))

print(b[0, 1])

print(b[:, 1])

print(b[:, 1:3])

print(b < 5)

print(b[b < 5])

b[b < 5] = 0
print(b)

print(np.sort(b))

a = np.random.randint(0, 10, 5)
print(a)

np.sort()
