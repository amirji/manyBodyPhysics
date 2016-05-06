import numpy as np
import convertToBitPattern as bit

f = open('E_lRaw.dat', 'r');
temp = f.read().splitlines();
temp = [float(i) for i in temp];

E_lRaw = np.array(temp);
E_l = E_lRaw[E_lRaw != 0];

lengthEl= np.size(E_l);

N = int(np.log2(np.size(E_lRaw)));

trueStateSum = np.sum(E_l)/2**(N-1);
trueState = [];

for i in range (2**lengthEl):
    temp = bit.convert(i, lengthEl);
    bitPattern = np.array(temp);
    if (np.sum(bitPattern) == N):
       fakeState = bitPattern*E_l;
       if (np.sum(fakeState)) == trueStateSum:
           trueState = fakeState[fakeState != 0 ];
if np.size(trueState) == 0:
    print("The given set could not represent by single-particle spectrum.")
else:
    print(trueState);

