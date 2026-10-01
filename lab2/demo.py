import pandas as pd
df = pd.read_csv('Iris.csv')
print(df)
print(df.head(10))
print(df.tail(10))
df.shape
dup_df=pd.concat([df, df])
print(dup_df.shape)
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)

print(df.describe())

