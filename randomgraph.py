import random
import matplotlib.pyplot as plt


x = []
y = []

for i in range(0,10):
    x += [random.randint(0,10)]
    y += [random.randint(0,10)]


print(x)
print(y)

plt.scatter(x,y)
plt.show()