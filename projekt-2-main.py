"""Computernumerik - Übungsabgabe 2 - Gaußquadratur"""
from projekt2module import *

def tf1(x):
    return np.exp(x)
vgl1 = np.exp(1)-1

def tf2(x):
    return np.exp(10*x)
vgl2 = 1/10*(np.exp(10)-1)

def tf3(x):
    return (x**5)
vgl3 = 1/6

def tf4(x):
    return(np.sin(1000*np.pi*x))
vgl4=0

def tf5(x):
    return (1/(0.01*np.sqrt(2*np.pi))*np.exp(-1/2*((x-0.5)/0.01)**2))
vgl5=1

#plot(tf1,4,40,vgl1, G_Wert=3, name="G3-tf1", plottitle="Fehler der G3 Funktion für "+r"$f_1(t)$")
#plot(tf2,4,45,vgl2, G_Wert=3, name="G3-tf2", plottitle="Fehler der G3 Funktion für "+r"$f_2(t)$")
#plot(tf4,4,35,vgl4, G_Wert=3, name="G3-tf4", plottitle="Fehler der G3 Funktion für "+r"$f_4(t)$")
#plot(tf5,4,40,vgl5, G_Wert=3, name="G3-tf5", plottitle="Fehler der G3 Funktion für "+r"$f_5(t)$")




#plot(tf1,0,20,vgl1, G_Wert=5, name="G5-tf1", plottitle="Fehler der G5 Funktion für "+r"$f_1(t)$")
plot(tf2,4,18,vgl2, G_Wert=5, name="G5-tf2", plottitle="Fehler der G5 Funktion für "+r"$f_2(t)$")
#plot(tf5,4,40,vgl5, G_Wert=5, name="G5-tf5", plottitle="Fehler der G5 Funktion für "+r"$f_5(t)$")


