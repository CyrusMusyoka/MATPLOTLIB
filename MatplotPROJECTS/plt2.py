import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

print("x data points are as following :\n", x_data)
print("***********************************************")
print("y_data points are as following :\n", y_data)

plt.scatter(x_data, y_data)

plt.show()