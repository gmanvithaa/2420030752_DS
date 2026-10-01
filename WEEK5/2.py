import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
from sklearn.decomposition import PCA

tips = sns.load_dataset('tips')

print("Original Data:")
print(tips.head())

numeric_cols = tips.select_dtypes(include=['float64', 'int64']).columns

scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols] = scaler_minmax.fit_transform(tips[numeric_cols])

print("\nNormalized Data:")
print(tips_normalized.head())

scaler_standard = StandardScaler()
tips_standardized = tips.copy()
tips_standardized[numeric_cols] = scaler_standard.fit_transform(tips[numeric_cols])

print("\nStandardized Data:")
print(tips_standardized.head())

tips = sns.load_dataset('tips')

numeric_cols = tips.select_dtypes(include=['float64', 'int64']).columns

scaler = StandardScaler()
tips_standardized = tips.copy()

scaled_data = scaler.fit_transform(tips_standardized[numeric_cols])

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

print("\nPCA Result:")
print(pca_df.head())

import matplotlib.pyplot as plt
plt.scatter(pca_df['PC1'], pca_df['PC2'],alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Tips Dataset')
plt.show()