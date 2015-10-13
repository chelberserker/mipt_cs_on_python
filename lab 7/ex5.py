import numpy as np
import matplotlib.pyplot as plt
def f(x, l):
	y = eval(l)
	return y
	

func = input()	
x=np.arange(-10,10,0.01)
y = [f(_x, func) for _x in x]
plt.xkcd()
plt.plot(x, y)
plt.show()
