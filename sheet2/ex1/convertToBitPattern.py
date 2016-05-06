def convert(x,N):
    n = [0]*N
    i = 0
    while x >= 2:
        n[i]=(x%2)
        x = int(x/2)
        i += 1
    n[i] = x
    return n
