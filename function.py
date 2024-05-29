import numpy as np
from numpy import exp
import matplotlib.pyplot as plt

def tf7(x):
    return (1/(0.01*np.sqrt(2*np.pi))*np.exp(-1/2*((x-0.5)/0.01)**2))

plt.plot(np.arange(0, 1, 0.0001), tf7(np.arange(0, 1, 0.0001)))

plt.show()