import pandas as pd

df = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/HaploStats EURCAU/fauxneg2/count_allele/eurcau_all.xlsx")

df.value_counts().to_excel('/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/HaploStats EURCAU/fauxneg2/count_allele/eurcau_all_count.xlsx')


df2 = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/HaploStats EURCAU/fauxneg2/count_allele/eurcau_all_count.xlsx")           
index_names = df2[ df2['A1_T'] == df2['A1_P']  ].index
  
# drop these row indexes
# from dataFrame
df2.drop(index_names, inplace = True)
df2.to_excel("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/HaploStats EURCAU/fauxneg2/count_allele/eurcau_all_count2.xlsx")