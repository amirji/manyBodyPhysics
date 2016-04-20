import numpy as np

def matrix(Tin,w):
    M = Tin.copy()
    N = len(M)

    for i in range(N):
        for j in range(N):
            M[i,j] = w*M[i,j]*delta(i+1,j+1) + delta(i+1,j+2) + delta(i+2,j+1)
    return M


def delta(i, j):
    if i == j:
        return 1.0
    else:
        return 0.0

