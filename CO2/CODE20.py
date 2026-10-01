import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\Lenovo\\OneDrive\\ドキュメント\\DS\\CO2\\temporal.csv')
sns.boxplot(df['data science'])
plt.show()
