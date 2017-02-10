import matplotlib.pyplot as plt
import numpy as np

x = np.arange (-5, 5.01, 0.01)
d = np.arange (-5, 6, 1)

plt.plot(x, x*x-x-6, d, d*0, 'bo')
plt.grid(True)
plt.show() 
