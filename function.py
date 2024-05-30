import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from fractions import Fraction

# Sample data
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x)

# Function to format x-ticks as fractions
def fraction_formatter(x, pos):
    frac = Fraction(x).limit_denominator()
    return f'{frac}'

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Apply the formatter to the x-axis
formatter = FuncFormatter(fraction_formatter)
ax.xaxis.set_major_formatter(formatter)

# Adjust the ticks location (optional)
ax.set_xticks(np.linspace(0, 1, 11))

plt.show()
