import numpy as np
from scipy.integrate import simps
import pandas as pd 

#Define
h = 1/2

a = 0
b = 1

# Gauss-Integration

#n=3
n=3
x = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
alpha = [5/9, 8/9, 5/9]

#transform coeffizients

x_h = [0] * 3
alpha_h = [0] * 3

G_h = 0

def f(x):
    return np.exp(x)

i = 0
while(i<1):
    k = 0

    a_h = i
    b_h = a_h +h

    #Berechne Koeffizienten
    for k in range(0, n-1):
        print("k: %s" % k)
        x_h[k] = (b_h-a_h)/2 *x[k] + (a_h+b_h)/2
        alpha_h[k] = (b_h-a_h)/2 * alpha[k]
        print("x_h_%s: %s, alpha_h_%s: %s" % (k, x_h[k], k, alpha_h[k]))

        G_h += f(x_h[k])*alpha_h[k]

    print("a_h: %s b_h: %s " % (a_h, b_h))



    i+=h

print("G_h: %s" % G_h)
