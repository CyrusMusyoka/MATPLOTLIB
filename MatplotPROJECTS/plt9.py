import numpy as np
import matplotlib.pyplot as plt

height = np.random.normal(172, 8, 300)
print(height)
plt.boxplot(height)
plt.show()