import matplotlib.pyplot as plt
from random import random

data = [random() for i in range(10000)]
plt.hist(data, bins=100)
plt.show()
