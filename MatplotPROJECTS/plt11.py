import numpy as np
import matplotlib.pyplot as plt

years = [2014 + x for x in range (8)]
print(years)

income = [55, 56, 62, 61,
          72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title("Income of Cyrus in 8yrs (in USD)", fontsize = 20)
plt.xlabel("years")
plt.ylabel("Yearly income in USD ")
plt.yticks(income_ticks, [f"${x}k USD" for x in income_ticks])

plt.show()