import matplotlib.pyplot as plt
from random import random
input = open('float_data.txt', 'r')
data = input.readlines()
for i in range(len(data)):
	data[i] = float(data[i])
plt.hist(data, bins=20)
plt.show()
