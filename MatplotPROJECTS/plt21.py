import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

x = np.arange(0, 50, 0.1)
y = np.sin(x)
print("y plots are : ", y)
z = np.cos(x)
print("z points are: " ,z)

ax.plot(x, y, y)
ax.set_title("3D Plot")
ax.set_xlabel("test")

plt.show()