import pandas as pd
import numpy as np
df = pd.DataFrame({'Age': [25, 30, 35, 40], 'Department': ['HR', 'IT', 'Finance', 'Marketing']})

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
print(df)