import numpy as np

x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])

v = np.array([1,0,1])
y = np.zeros(x.shape)

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        y[i,j] = x[i,j] + v[j]

print(y)