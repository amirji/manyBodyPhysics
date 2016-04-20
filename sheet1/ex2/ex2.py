import derivationF as entropy
import numpy as np
import matplotlib.pyplot as plt

L = [10,100,1000]
T = np.arange(0.0, 20.0 , 0.01)

S1 = entropy.S(T, L[0])
S2 = entropy.S(T, L[1])
S3 = entropy.S(T, L[2])

plt.plot(T,S1,'r', T,S2,'b', T,S3,'g')


plt.xlabel('tempreture (T)')
plt.ylabel('entropy (J/K)')
plt.title('The entropy with L=10,100,1000')
plt.grid(True)
plt.savefig("entropy.png")
plt.show()
