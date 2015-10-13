import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return x*x-6-x
x=np.arange(-10,10,0.01)
plt.plot(x, f(x))
for i in x:
	if -0.01 <= f(i) <= 0.01:
		print(i)
plt.show()
