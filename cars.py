import pandas as pd
import numpy as np

#Load dataset into a Pandas DataFrame
df = pd.read_csv('mtcars.csv')
df = df.set_index('model')

#1
test_rows = df.head(5)
shape = df.shape
#print(df)
#print(shape)
#There are 32 rows and 11 columns
#2
col_dt_types = df.dtypes
#print(col_dt_types)

#3
test_mpg = df['mpg']
avg_mpg = df['mpg'].mean()
#print(test_mpg)
#print("\nAverage mpg:", avg_mpg) #Average is 20.090625

#4
test_describe = df.describe()
max_hp = df['hp'].max() 
max_hp_car = df[df['hp'] == 335]
#print(max_hp_car)
#print(max_hp)
#A: Max hp car is the Maserati Bora

#5
mpg25 = df[df['mpg'] > 25]
mpg20_10 = df[df['mpg'].between(20, 100)]
#print(mpg25)
#print(mpg20_10)

#6
first5 = df[['mpg', 'hp',  'wt']].head(5)
#print(first5)

#7
toyota = df.loc['Toyota Corolla']
#print(toyota)

#8
mpg_descend = df['mpg'].sort_values(ascending=False)
#print(mpg_descend)
#A: Toyota Corolla > Fiat 128 > Lotus Europa

#9
weight_rank = df['wt'].sort_values(ascending=True)
#print(weight_rank)

#10
avg_mpg_by_cyl = df.groupby('cyl')['mpg'].mean()
avg_hp__by_cyl = df.groupby('cyl')['hp'].mean()
#print(avg_mpg_by_cyl)
#for 4 cyls: 26.66, 6 cyls: 19.74, 8 cyls: 15.10, 
#print(avg_hp__by_cyl)
#for 4 cyls: 82.64, 6 cyls: 122.26, 8 cyls: 209.21,
 
#11
max_hp_by_cyl = df.groupby('cyl')['hp'].max()
#print(max_hp_by_cyl)

#12
df['power_to_weight'] = df['hp'] / df['wt']
print(df)
max_hp_to_wt_car = df['power_to_weight'].idxmax()
print("Car with highest power to weight ratio:", max_hp_to_wt_car)
#A: The car with highest power to weight ratio is the Maserati Bora
# 
#This was cool 