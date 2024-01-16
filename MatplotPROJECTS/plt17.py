# plotting different figures same page
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

#style.use("dark_background")

x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)


plt.show()