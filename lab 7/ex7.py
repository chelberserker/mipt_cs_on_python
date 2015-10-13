import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	s = 0 
	b = 0.5
	a = 3
	for n in range(1, 50):
		s += (b**n)*(math.cos((a**n)*(math.pi)*x)) 
	y = s
	return y
	

x=np.arange(-2,2,0.01)
y = [f(_x) for _x in x]
plt.grid(True)
plt.plot(x, y)
plt.show()
