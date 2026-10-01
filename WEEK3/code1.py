import pandas as pd
import numpy as np
from scipy.stats import spearmanr
df = pd.DataFrame({'X': [1, 2, 3, 4, 5],
                   'Y': [10, 20, 30, 40, 50]})

corr_matrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", corr_matrix)

dff = pd.DataFrame({'DS': [100, 80, 60, 89, 98],
                    'CD': [100, 80, 90, 40, 50],
                    'TOC': [100, 80, 90, 40, 50]}) 
corr_matrix2 = dff.corr(method='pearson')
print("\nPearson Correlation Matrix for dff:\n", corr_matrix2)




dff3 = pd.DataFrame({'X': [100, 80, 60, 89, 98],
                     'Y': [100, 80, 90, 40, 50],})
corr_value, p_value = spearmanr(dff3['X'], dff3['Y'])
print("\nSpearman Correlation Coefficient:", corr_value)
print("Spearman p-value:", p_value)

dff4 = pd.DataFrame({'CD': [100, 80, 60, 89, 98],
                     'TOC': [100, 80, 90, 40, 50],  
                     'DS': [100, 80, 90, 40, 50]})  
corr_value2, p_value2 = spearmanr(dff4['CD'], dff4['TOC'])
print("\nSpearman Correlation Coefficient:", corr_value2)
print("Spearman p-value:", p_value2)



