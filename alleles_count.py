import pandas as pd

df = pd.read_excel("path.xlsx")

df.value_counts().to_excel('path_count.xlsx')


df2 = pd.read_excel("path_count.xlsx")           
index_names = df2[ df2['_T'] == df2['_P']  ].index
  
# drop these row indexes
# from dataFrame
df2.drop(index_names, inplace = True)
df2.to_excel("path_count2.xlsx")
