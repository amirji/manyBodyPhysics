import setupMatrix as setup
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

eigenValue = []
eigenVector =[]
Tfixed =[0][0]
eNumbers = 10
N = 30
eValue = [0]*eNumbers
eVector = [0]*eNumbers

w = np.linspace(0.0,5.0 , eNumbers)
T = 2*np.random.random_sample((N,N))-1.0

for i in range(10):
    Tout = setup.matrix(T,w[i]).copy()
    eValue, eVector = LA.eig(Tout)
    index = eValue.argsort()[::1]
    eValue = eValue[index]
    eVector = eVector[:,index]
    eigenValue.append(eValue)
    eigenVector.append(eVector)

plt.plot(w, eigenValue)
plt.xlabel('w')
plt.ylabel('eigenValue')
plt.title('The eigenValue vs w with N=30')
plt.grid(True)
plt.savefig("eigenValue30.png")
plt.show()

print(w, v)
