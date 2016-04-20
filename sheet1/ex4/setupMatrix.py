import numpy as np

def matrix(T,w):
    N = len(T)

    for i in range(N):
        for j in range(N):
            T[i,j] = w*T[i,j]*delta(i+1,j+1) + delta(i+1,j+2) + delta(i+2,j+1)
    return T


def delta(i, j):
    if i == j:
        return 1.0
    else:
        return 0.0

