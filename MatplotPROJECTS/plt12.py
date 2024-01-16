import numpy as np
import matplotlib.pyplot as plt

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [98, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]

plt.plot(stock_a, label = "Tesla")
plt.plot(stock_b, label = "Apple")
plt.plot(stock_c, label = "Amazon")

# displays the labels of each plots
#plt.legend()

plt.legend(loc = "lower center")
# showing each label plot on lower location


plt.title("Stock Graph Plot")
plt.show()
