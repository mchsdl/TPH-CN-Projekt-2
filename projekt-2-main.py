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

def tf7(x):
    return (1/(0.01*np.sqrt(2*np.pi))*np.exp(-1/2*((x-0.5)/0.01)**2))
vgl7=1

plot(tf1,4,40,vgl1,name="G3-tf1")
#plot(tf2,4,40,vgl2,name="G3-tf2")
#plot(tf3,0,40,vgl3,name="G3-tf3")
#plot(tf4,4,40,vgl4,name="G3-tf4")
#plot(tf5,0,40,vgl5,name="G3-tf5")
#plot(tf6,4,45,vgl6,name="G3-tf6")
#plot(tf7,4,45,vgl7,name="G3-tf7")

#plot(tf1,0,40,vgl1,G_Wert= 5,name="G5-tf1")
#plot(tf2,0,40,vgl2,G_Wert= 5,name="G5-tf2")
#plot(tf3,0,40,vgl3,G_Wert= 5,name="G5-tf3")
#plot(tf4,4,40,vgl4,G_Wert= 5,name="G5-tf4")
#plot(tf5,0,40,vgl5,G_Wert= 5,name="G5-tf5")
#plot(tf6,4,45,vgl6,G_Wert= 5,name="G5-tf6")
#plot(tf7,4,45,vgl7,G_Wert= 5,name="G5-tf7")

