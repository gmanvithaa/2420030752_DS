import pandas as pd
import numpy as np
df = pd.DataFrame({'Age': [25, 30, np.nan, 40], 'Department': ['HR', 'IT', np.nan   , 'Marketing']})
print("Original Dataset (with missing values):")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print("Dataset after Forward Fill:")
print(df_ffill)

