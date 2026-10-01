import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40],
    'Department': ['HR', 'IT', np.nan, 'Marketing']
})

print("Original DataFrame:")
print(df)

df_drop_rows = df.dropna()


print(df_drop_rows)