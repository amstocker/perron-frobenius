import numpy as np
from numpy import linalg as la

N = 50

# We are guessing that the limit of the Perron-Frobenius
#   eigenvalues is sqrt(2).
guess = np.sqrt(2)

a = np.array([[0,1], [1,0]])

for i in range(1, N):
    prev = a
    
    a = np.zeros((2*i + 2, 2*i + 2))
    a[0:2*i, 0:2*i] = prev
    a[2*i, 2*i - 2] = 1
    a[2*i - 1, 2*i + 1] = 1
    a[2*i + 1, 2*i] = 1
    
    # spectral radius
    r = np.amax(np.absolute(la.eigvals(a)))
    print("{}:".format(i), r, "(error: {})".format(guess - r))