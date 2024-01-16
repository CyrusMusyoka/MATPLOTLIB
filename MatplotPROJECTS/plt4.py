import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weights = [79, 76, 79, 80, 84, 78, 81, 82, 83, 84, 87, 86, 89, 80, 90, 75]

print(len(years))
print("data points for years :", years)

print(len(weights))
print("data points for weights :", weights)


plt.plot(years, weights, marker = "*", c = "red",lw = "1.5", linestyle ="--")
# lw = linewidth
#plt.scatter(years, weights)
# linestyle appearance i.e "--"
plt.show()