import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45],})
print("Original Data:")
print(data)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
print("\nNormalized Data:")
print(normalized_df)
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)
standardized_df = pd.DataFrame(standardized_data, columns=data.columns)
print("\nStandardized Data:")
print(standardized_df)

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})
one_hot_encoded_df = pd.get_dummies(df, columns=['Color'])
print("\nOne-Hot Encoded Data:")
print(one_hot_encoded_df)
