import numpy as np
import matplotlib.pyplot as plt

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels = people)
plt.legend(labels = people)

plt.show()