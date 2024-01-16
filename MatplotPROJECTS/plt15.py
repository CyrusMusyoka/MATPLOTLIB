import numpy as np
import matplotlib.pyplot as plt

fahm = ['chelsea', 'arsenal', 'man utd', 'man city']

x = [3, 2, 2,1]

plt.pie(x, labels = fahm)
#plt.legend(labels = fahm)
plt.show()