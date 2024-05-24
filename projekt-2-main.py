"""Computernumerik - Übungsabgabe 2 - Gaußquadratur"""
from projekt2module import *

def tf1(x):
    return np.exp(x)
vgl1 = np.exp(1)-1

def tf2(x):
    return np.exp(10*x)
vgl2 = 1/10*(np.exp(10)-1)

def tf3(x):
    return (x**2)
vgl3 = 1/3

def tf4(x):
    return (1/(1+x**2))
vgl4 = np.arctan(1)

def tf5(x):
    return (np.log(x+1)/(x**2+1))
vgl5 = 1/8*np.pi*np.log(2)

def tf6(x):
    return(np.sin(1000*np.pi*x))
vgl6=0

plot(tf1,0,10,vgl1,save="images/G3-tf1.jpg")
plot(tf2,0,10,vgl2,save="images/G3-tf2.jpg")
plot(tf3,0,10,vgl3,save="images/G3-tf3.jpg")
plot(tf4,0,10,vgl4,save="images/G3-tf4.jpg")
plot(tf5,0,10,vgl5,save="images/G3-tf5.jpg")
plot(tf6,0,45,vgl6,save="images/G3-tf6.jpg")

plot(tf1,0,10,vgl1,G_Wert= 5,save="images/G5-tf1.jpg")
plot(tf2,0,10,vgl2,G_Wert= 5,save="images/G5-tf2.jpg")
plot(tf3,0,10,vgl3,G_Wert= 5,save="images/G5-tf3.jpg")
plot(tf4,0,10,vgl4,G_Wert= 5,save="images/G5-tf4.jpg")
plot(tf5,0,10,vgl5,G_Wert= 5,save="images/G5-tf5.jpg")
plot(tf6,0,45,vgl6,G_Wert= 5,save="images/G5-tf6.jpg")
