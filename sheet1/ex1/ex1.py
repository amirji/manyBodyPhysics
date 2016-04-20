import convertToBitPattern as bit

N = 6
n = []*N
E = [.0]*2**N

for j in range(0 , 2**N):
    n = bit.convert(j,N)
    for i in range (6):
        E[j] = E[j] + n[i]*(0.1*(i-2.5))
    print ('E(%d) = %f ' % (j,E[j]), 'with bit pattern',n)

# This algorithem can be faster if we just send the indexes of "1"s,
# since in this way the last iterator would be in general half of this amount.
# I also saved all E(l) in order to probably using this module in
# future programs.
