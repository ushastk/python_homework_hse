import numpy as np
a = np.zeros(25)
[0 for i in range(25)]

b = np.ones(10)
[1 for i in range(10)]

c = np.arange(12, 52)
[i for i in range(12, 52)]

d = np.arange(12, 52, 2)
[i for i in range(12, 52, 2)]

k = np.full(12, 5)
[5 for i in range(12)]

A = np.arange(1, 10)
B = A.reshape(3, 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

C = np.eye(5, 5)
[[1 for i in range(5)] for i in range(5)]

D = np.arange(0.01, 1.01, 0.01).reshape(10,10)
[[0 for j in range(10)] for i in range(10)]

E = np.arange(1, 26).reshape(5, 5)
e = E[2:,1:]
f = E[2, 4]
g = E[1:4, 1]
h = E[3:]
summa = np.sum(E)

summa1 = np.sum(E[:,0])
summa2 = np.sum(E[:,1])
summa3 = np.sum(E[:,2])
summa4 = np.sum(E[:,3])
summa5 = np.sum(E[:,4])
print(a, b, c, d, B, C, D, E, e, f, g, h, summa, summa1)