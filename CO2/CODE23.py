import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randint(1, 100, (10,10))
sns.heatmap(data,vmin=30,vmax=70)
plt.show()