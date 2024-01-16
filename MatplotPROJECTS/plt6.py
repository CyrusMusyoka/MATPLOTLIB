# ploting bar graph
import numpy as np
import matplotlib.pyplot as plt

# ploting a bar graph showing how different languages variations
x = ["Python", "Java", "C++", "R", "C", "C#"]
y = [40, 21, 18, 17, 26, 13]

plt.bar(x, y, align = "edge", color="brown", width = 0.5)
# align = where the bar starts
# edgecolor = "green" is still a way of styling
plt.show()