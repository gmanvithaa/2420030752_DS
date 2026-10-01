import pandas as pd
import numpy as np
df = pd.DataFrame({'Date': ['2023-01-01', '05/01/2023', 'Jan 1, 2023', '2023.01.04'], })
print("Original DataFrame:")
print(df)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')    
print("\nDataFrame after converting to datetime:")  
