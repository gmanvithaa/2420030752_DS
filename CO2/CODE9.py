import matplotlib.pyplot as plt
import numpy as np

values = [0, 1, 2, 3, 4, 5]
names = ["A", "B", "C", "D", "E", "F"]

plt.barh(names, values, color='red')

plt.title('Bar Plot of Deep Learning vs Machine Learning')
plt.xlabel('Deep Learning')
plt.ylabel('Machine Learning')

plt.grid()
plt.legend(['Data Points'])
plt.show()

