import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.read_csv("C:/Users/Lenovo/OneDrive/ドキュメント/DS/CO2/train.csv")

sns.lineplot(x=df.index, y="Weekly_Sales", data=df)

plt.xlabel("Index")
plt.ylabel("Weekly Sales")
plt.title("Line Plot of Weekly Sales")
plt.grid()

plt.show()