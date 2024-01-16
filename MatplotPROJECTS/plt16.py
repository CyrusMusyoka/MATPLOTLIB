# learning styling in matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# showinmg different color patterns
#style.use("ggplot")
# show type pf background color u want
style.use("dark_background")

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes)
plt.legend(labels = people)
plt.show()