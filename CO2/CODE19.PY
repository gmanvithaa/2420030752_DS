import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
import numpy as np
plt.boxplot(df['total_bill'])   
plt.show()