import math
def function(x):
	y = float(0)
	y = math.log((math.exp(1/(math.sin(x)+1)))/(5/4+1/(x**15)),1+x**2)
	return y
	

print(function(1), function(10), function(1000))
