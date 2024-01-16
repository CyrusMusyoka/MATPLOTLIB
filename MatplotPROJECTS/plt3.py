import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

plt.scatter(x_data , y_data , c = "#0f0", marker = "*")
# coloring
# use of c = "green" || c = "ofo" || c = "#0000"

# marker for ploting the graph
# marker = "*"
# size : s = 150
# lw = linewidth
# alpha = 0.3 used to make more clearer for data plots which are overlapping
plt.show()
print(x_data)
print(y_data)