import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.cos(x + y)


ax.plot(x, y, y)
ax.set_title("3D Plot")
ax.set_xlabel("test")

plt.savefig("3D projection")
plt.show()