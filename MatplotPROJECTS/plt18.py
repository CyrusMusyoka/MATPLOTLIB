import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


x = np.arange(100)

fig, axis =plt.subplots(2, 2)

axis[0, 0].plot(x, np.sin(x))
axis[0, 0].set_title("Sine Wave")

axis[0, 1].plot(x, np.cos(x))
axis[0, 1].set_title("Cosine Wave")

axis[1, 0].plot(x, np.random.random(100))
axis[1, 0].set_title("Random Function")

axis[1, 1].plot(x, np.log(x))
axis[1, 1].set_title("Log Function")
axis[1, 1].set_xlabel("TEST")

fig.suptitle("Four PLOTS")

plt.tight_layout()
plt.savefig("fourplots.png", dpi = 300,
            transparent=False)


plt.show()