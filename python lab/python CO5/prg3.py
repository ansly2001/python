import pandas as pd
df=pd.read_csv("student detail1.csv",usecols=["roll no","name"])
print(df)
specific_column=df[["name","class"]]
print(specific_column)
print(df.head())
print(df.tail())
