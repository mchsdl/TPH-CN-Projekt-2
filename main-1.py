"""Computernumerik - Übungsabgabe 2 - Gaußquadratur"""
import numpy as np
import matplotlib.pyplot as plt

def efunktion1(x):
    return np.exp(x)

def efunktion2(x):
    return np.exp(10*x)

def funktion3(x):
    return (np.log(x+1)/(x**2+1))

x3=[-np.sqrt(3/5),0,np.sqrt(3/5)]
a3=[5/9,8/9,5/9]

x5 = [-1/3*np.sqrt(5+2*np.sqrt(10/7)), -1/3*np.sqrt(5-2*np.sqrt(10/7)), 0, 1/3*np.sqrt(5-2*np.sqrt(10/7)), 1/3*np.sqrt(5+2*np.sqrt(10/7))]
a5 = [(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900]

def G3(h,funktion):
    schritt = np.arange(0,1,step=h)
    
    summe = 0
    for i in range(len(schritt)):
        for j in range(3):
            summe += h/2*funktion(h/2*x3[j]+schritt[i]+h/2)*a3[j]
    
    return summe

lsg1 = []
lsg2 = []

for i in range(4,20):
    lsg1.append(G3(1/(i+1),efunktion1)-(np.exp(1)-1))

for i in range(4,20):
    lsg2.append(G3(1/(i+1),funktion3)-(1/8*np.pi*np.log(2)))

plt.figure(dpi=300)

plt.xscale("log")

plt.plot(np.arange(len(lsg2))+1,lsg2)
#plt.plot(np.arange(len(lsg2))+1,lsg2)

plt.savefig("G3-1.png")
