import pandas as pd
import numpy as np
df = pd.DataFrame({'Id': [1, 2, 3, 4], 'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})
df_subset_ID = df.drop_duplicates(subset='Id')
print(df_subset_ID)
df_subset_Name = df.drop_duplicates(subset='Name')
print(df_subset_Name)