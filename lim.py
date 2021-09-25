import numpy as np
from numpy import linalg as la

N = 100
guess = np.sqrt(2)

A0 = np.array([[0,1], [1,0]])

A = A0
lastA = A
for i in range(1, N):
    A = np.zeros((2*i + 2, 2*i + 2))
    A[0:2*i, 0:2*i] = lastA
    A[2*i, 2*i - 2] = 1
    A[2*i - 1, 2*i + 1] = 1
    A[2*i + 1, 2*i] = 1
    lastA = A
    l = np.amax(np.absolute(la.eigvals(A)))
    print("{}:".format(i), l, "(error: {})".format(guess - l))