import numpy as np
import matplotlib.pyplot as plt

langs = ["python", "C#", "R", "Java", "C++", "C", "Go"]
votes = [60, 50, 55, 30, 17, 48, 53]
explodes = [0.3, 0, 0, 0, 0.1, 0, 0]

plt.pie(votes, labels = langs ,explode = explodes,
        autopct = "%.2f%%" , startangle = 90)
# startangle = 90 / ploting of the piechart start at 90 degree
plt.show()