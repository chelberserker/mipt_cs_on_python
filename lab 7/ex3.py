import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return math.log((x**2+1)*math.exp(-math.fabs(x)/10),(1+math.tan(1/(1+(math.sin(x))**2))))


x=np.arange(-10, 10, 0.01)
y = [f(_x) for _x in x]
plt.plot(x, y)
plt.show()
