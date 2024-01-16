import numpy as np
import matplotlib.pyplot as plt

clubs = ["chelsea", "man utd", "arsenal", "mancity", "liverpool", "tottenham"]

fans = [3000000, 4000000, 2500000, 500000, 1400000, 1000000]
explodes = [0, 0 , 0 , 0.3, 0, 0]
plt.pie(fans, labels = clubs, explode = explodes )
#plt.bar(clubs, fans)
plt.title("***Top 6 club's Fanbase around Africa***")
plt.show()
