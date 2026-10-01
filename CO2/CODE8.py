import matplotlib.pyplot as plt
import numpy as np
x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, color='red', marker="^")
plt.title('Scatter Plot of Deep Learning vs Machine Learning')
plt.xlabel('Deep Learning')
plt.ylabel('Machine Learning')  
plt.grid()
plt.show()
plt.legend(['Data Points'])
