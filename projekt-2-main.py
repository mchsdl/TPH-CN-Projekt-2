"""Computernumerik - Übungsabgabe 2 - Gaußquadratur"""
from projekt2module import *

def tf2(x):
    return (1/(1+x**2))
vgl2 = np.arctan(1)


plot(tf2,0,10,vgl2,save="images/G3-tf2.jpg")

