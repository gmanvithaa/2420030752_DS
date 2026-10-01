import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40],
    'Department': ['HR', 'IT', np.nan, 'Marketing']
})

df_dfill = df.copy()
df_dfill = df_dfill.bfill()

print("Dataset after Backward Fill:")
print(df_dfill)