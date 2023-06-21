import numpy as np

a = np.arr([[1, 1, 1], [2, 5, -1], [2, -1, 3]])
b = np.arr([6, -4, 27])

result = np.linalg.solve(a, b)
print(result)
c = np.loadtxt('input.txt', delimiter=' ', usecols=(0, 1, 2))
d = np.loadtxt('input.txt', delimiter=' ', usecols=(3,))

result_2 = np.linalg.solve(c, d)
print(result_2)