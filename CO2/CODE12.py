import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.pairplot(data, hue="sex", palette="Set1")
plt.title("Pair Plot of Tips Dataset")  
plt.show()
