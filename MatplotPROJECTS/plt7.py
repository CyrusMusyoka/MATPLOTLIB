# generating an histogram
import numpy as np
import matplotlib.pyplot as plt

edges = np.random.normal(20, 1.5, 1000)
print(edges)
plt.hist(edges,
         bins = 20,
         cumulative = True)
plt.show()