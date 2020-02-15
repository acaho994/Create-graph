import random


points = []

for i in range(0,10):
    for j in range(0,10):
        x = random.randint(0,10)
        y = random.randint(0,10)
    points += [(x,y)]


## value = random.randint(0,10)



print(points)