import numpy as np
import matplotlib.pyplot as plt

# x datapoints plotted in a array using range showing from 1 - 10
x = [1 + s for s in range(10)]
print(len(x))
y = [5 + m for m in range(10)]
print(len(y))

plt.plot(x, y, c = "green", marker = ".", lw = 2.3)
# plt.scatter()
plt.show()