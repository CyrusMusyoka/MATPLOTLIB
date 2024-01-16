import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

print("The x_data datapoints: \n", x_data)
plt.scatter(x_data, y_data)
plt.show()
