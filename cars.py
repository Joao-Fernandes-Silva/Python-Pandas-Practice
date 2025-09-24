import pandas as pd
import numpy as np

df = pd.read_csv('mtcars.csv')
test_rows = df.head(5)
test_mpg = df['mpg']
avg_mpg = df['mpg'].mean()
test_describe = df.describe()
max_hp = df['hp'].max()
mpg25 = df[df['mpg'] > 25]
mpg20_10 = df[df['mpg'].between(20, 100)]
toyota = df.loc['Toyota Corolla']

#print(df)
##print(test_rows)
#print(test_mpg)
#print("\nAverage mpg:", avg_mpg)
#print(test_describe)
#print("\nMax horsepower: ", max_hp)
#print(mpg25)
#print(mpg20_10)
print(toyota)