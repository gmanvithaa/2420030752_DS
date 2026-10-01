import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
x = np.random.rand(100)
y = np.random.rand(100)
sns.kdeplot(x=x, y=y, shade=True, color="blue", label="X")
plt.show()