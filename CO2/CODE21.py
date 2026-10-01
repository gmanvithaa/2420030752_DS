import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Lenovo\\OneDrive\\ドキュメント\\DS\\CO2\\temporal.csv')
Q1=np.percentile(df['data science'],25,method='midpoint')
Q3=np.percentile(df['data science'],75,method='midpoint')
IQR=Q3-Q1
print("the output of Q1 is:",Q1)
print(IQR)
