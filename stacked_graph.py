import matplotlib.pyplot as plt
import numpy as np

men_nums = (40,46,48,30,42)
women_nums = (40,42,45,50,47)
x_points = np.arange(1,6)

p1 = plt.bar(x_points,men_nums,0.5,)
p2 = plt.bar(x_points,women_nums,0.5,bottom=men_nums)


plt.legend((p1,p2),('Men','Women'))
plt.ylabel('Overall Score')
plt.xlabel('Group number')

plt.show()