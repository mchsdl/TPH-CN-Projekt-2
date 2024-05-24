"""Computernumerik - Übungsabgabe 2 - Gaußquadratur"""
import numpy as np

x3=[-np.sqrt(3/5),0,np.sqrt(3/5)]
a3=[5/9,8/9,5/9]

def G3(h,funktion):
    schritt = np.arange(0,1,step=h)
    
    summe = 0
    for i in range(len(schritt)):
        for j in range(3):
            summe += h/2*funktion(h/2*x3[j]+schritt[i]+h/2)*a3[j]
    
    return summe

def efunktion1(x):
    return np.exp(x)

def efunktion2(x):
    return np.exp(10*x)

print(G3(1,efunktion2))

import matplotlib.pyplot as plt

lsg1 = []
lsg2 = []
for i in range(4,20):
    lsg1.append(G3(1/(i+1),efunktion1)-(np.exp(1)-1))

for i in range(4,20):
    lsg2.append(G3(1/(i+1),efunktion2)-1/10*(np.exp(10)-1))

plt.figure(dpi=300)

plt.plot(np.arange(len(lsg1))+1,lsg1)
#plt.plot(np.arange(len(lsg2))+1,lsg2)


