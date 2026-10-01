import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
n2 = np.array([6, 7, 8, 9, 10])
print(np.sum([n1, n2], axis=0))
print(np.sum([n1, n2], axis=1))

