import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("/home/amanda/Documents/Python Scripts/snowfall.csv",names=True,dtype=None,delimiter=",",encoding="UTF-8")

plt.bar(data["Season"],data["Total_snowfall_in"])

plt.xlabel("Season")
plt.ylabel("Total inches")
plt.title("Snowfall by Season")

plt.show()
