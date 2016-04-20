import numpy as np

def Free(T, L):

    kb = 1.0
    beta = 1.0/(kb*T)

    Z = 0.0
    for l in range (1, L+1):
        E_l= np.sqrt(l)
        Z = Z + np.exp(-beta*E_l)

    F = -kb*T*np.log(Z)
    return F
 
