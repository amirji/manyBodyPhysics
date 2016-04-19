import convertToBitPattern as bit

N = 6
n = []*N
E = [.0]*2**N

for j in range(0 , 2**N):
    n = bit.convert(j,N)
    for i in range (6):
        E[j] = E[j] + n[i]*(0.1*(i-2.5))
    print ('E(%d) = %f ' % (j,E[j]), 'with bit pattern',n)
