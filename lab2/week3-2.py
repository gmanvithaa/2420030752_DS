import pandas as pd
data = [1, 2, 3, 4, 5,10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data = {'Name': ['JJ', 'AA', 'BB', 'EE'],
        'Age': [25, 30, 22, 28]
        }
df = pd.DataFrame(data)
print(df)
df.to_csv('sample1.csv', index=True)