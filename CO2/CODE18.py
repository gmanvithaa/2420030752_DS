import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")
sns.kdeplot(data=df  )

plt.show()