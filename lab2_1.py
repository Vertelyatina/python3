import numpy as np
for x in [1, 10, 1000]:
	print(np.log(1/np.e**(np.sin(x)+1))/np.log(1+x**2)-np.log(5/4+1/x**15)/np.log(1+x**2))
