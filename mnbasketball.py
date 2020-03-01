import numpy as np 
import matplotlib.pyplot as plt

data = np.genfromtxt("/home/amanda/Documents/Python Scripts/MNbasketball.csv",names=True,dtype=None,delimiter=",",encoding="UTF-8")
x_points = np.arange(1,28)
y_points = data["MNScore"]
homes = data["H_A"]
print(homes)

# use a square if the game was at home
# use a triangle if the game was away
markers = []
for i in data["H_A"]:
    if i == "H":
        markers += ["s"]
    else:
        markers += ["^"]
# make the icon green if it was a win
# make the icon red if it was a loss
colors = []
for j in data["W_L"]:
    if j == "W":
        colors += ['g']
    else:
        colors += ['r']

print(y_points)

## print(data)

plt.scatter(x_points,y_points,marker=markers,c=colors)
plt.show()