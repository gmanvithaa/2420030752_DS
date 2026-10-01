import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")
sns.kdeplot(data=df['petal_length'], shade=True, color="blue", label="Petal Length")
plt.show()