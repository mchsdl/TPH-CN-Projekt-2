"""Computernumerik - Übungsabgabe 2 - Gaußquadratur - Modul"""
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt

def G3(h,funktion):
    schritt = np.arange(0,1,step=h)
    x3=[-np.sqrt(3/5),0,np.sqrt(3/5)]
    a3=[5/9,8/9,5/9]
    summe = 0
    for i in range(len(schritt)):
        for j in range(3):
            summe += h/2*funktion(h/2*x3[j]+schritt[i]+h/2)*a3[j]
    return summe

def G5(h,funktion):
    schritt = np.arange(0,1,step=h)
    x5 = [-1/3*np.sqrt(5+2*np.sqrt(10/7)),-1/3*np.sqrt(5-2*np.sqrt(10/7)),
          0, 1/3*np.sqrt(5-2*np.sqrt(10/7)), 1/3*np.sqrt(5+2*np.sqrt(10/7))]
    a5 = [(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225,
          (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900]
    summe = 0
    for i in range(len(schritt)):
        for j in range(5):
            summe += h/2*funktion(h/2*x5[j]+schritt[i]+h/2)*a5[j]
    return summe

def plot(Testfunktion,nmin,nmax,Vergleichsintegralwert,G_Wert=3,log=False,save=False):
    tf,vgl = Testfunktion, Vergleichsintegralwert

    h,err = [],[]
    for i in range(nmin,nmax):
        h.append(1/(i+1))
        if G_Wert==3:
            err.append(G3(1/(i+1),tf)-vgl)
        elif G_Wert==5:
            err.append(G5(1/(i+1),tf)-vgl)
        else:
            print("Fehlermeldung")
            break
    h.reverse()
    err.reverse()

    plt.figure(dpi=500)
    plt.plot(h,err,"-r")

    if log:
        plt.xscale("log")
    
    if save:
        plt.savefig(save)
        
    return 0




plot(exp,0,4,exp(1)-1,save="images/testplot.jpg")