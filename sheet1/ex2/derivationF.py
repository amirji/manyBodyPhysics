import freeEnergy as energy

def S(T, L):

    h = 0.0000000001
    entropy = ( energy.Free(T+h, L) - energy.Free(T-h, L) )/(2*h)

    return entropy
