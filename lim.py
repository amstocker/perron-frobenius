import numpy as np
from numpy import linalg as la

N = 100
guess = np.sqrt(2)

a = np.array([[0,1], [1,0]])

prev = a
for i in range(1, N):
    a = np.zeros((2*i + 2, 2*i + 2))
    a[0:2*i, 0:2*i] = last
    a[2*i, 2*i - 2] = 1
    a[2*i - 1, 2*i + 1] = 1
    a[2*i + 1, 2*i] = 1
    last = a
    r = np.amax(np.absolute(la.eigvals(a)))
    print("{}:".format(i), r, "(error: {})".format(guess - r))