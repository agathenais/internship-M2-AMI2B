import itertools
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

A = ["DQB1*02:01", "DQB1*02:02", "DQB1*04:01", "DQB1*04:02" , "DQB1*05:01", "DQB1*05:02", "DQB1*06:01", "DQB1*06:02", "DQB1*06:03", "DQB1*06:04", "DQB1*06:09", "DQB1*03:01", "DQB1*03:02", "DQB1*03:03"]
B = list(itertools.product( A, repeat=2))
pd.Series(B).to_csv('/Users/agathenaisadiguna/Downloads/combinaison.csv')

C = pd.read_excel("/Users/agathenaisadiguna/Downloads/combinaison.xlsx")
D= pd.read_excel("/Users/agathenaisadiguna/Downloads/DQB1_input2.xlsx")
names=['ID_T', 'DQB1_T', 'ID_P', 'DQB1_P']
pd.DataFrame(C,columns=names).to_excel("/Users/agathenaisadiguna/Downloads/cgrsfed.xlsx")


pd.read_csv('/Users/agathenaisadiguna/Downloads/DQB1.txt', sep=" ").to_csv("/Users/agathenaisadiguna/Downloads/DQB1.csv")
df = pd.read_excel("/Users/agathenaisadiguna/Downloads/DQB1_input_clustermap.xlsx")
df.pivot(index='DQB1_T', columns='DQB1_P', values='Count').to_csv("/Users/agathenaisadiguna/Downloads/DQB1_input_clustermap.csv")


df = pd.read_excel("/Users/agathenaisadiguna/Downloads/prematrix2.xlsx")
df.pivot_table(columns='DQB1_P', index='DQB1_T', values='Count').reset_index().to_csv("/Users/agathenaisadiguna/Downloads/matrix2.csv")

data = pd.read_excel('/Users/agathenaisadiguna/Downloads/DQB1_input_clustermap.xlsx')
data2= pd.read_excel('/Users/agathenaisadiguna/Downloads/matrix2.xlsx')
cluster_map = sb.clustermap(data2)

A = [[1.0,16.0,11.0,13.0,15.0,14.0,11.0,12.0,15.0,13.0,12.0,13.0,13.0], 
    [0,17.0, 12.0, 14.0,16.0 , 15.0      ,  12.0     ,   13.0    ,    16.0 ,      14.0    ,    13.0   ,     14.0   ,     14.0],
    [0      ,     0    ,     7.0  ,       4.0    ,       0     ,      0     ,      0      ,     0    ,       0     ,      0     ,      0      ,     0     ,      0],
    [0     ,      0    ,       0  ,       3.0    ,       0      ,     0      ,     0      ,     0   ,        0      ,     0      ,     0    ,       0    ,       0],
    [0   ,     14.0    ,   10.0     ,    9.0   ,        0    ,     1.0    ,    16.0   ,     16.0     ,   16.0  ,      11.0    ,    12.0   ,     14.0     ,   14.0],
    [0    ,    13.0    ,     9.0     ,    8.0   ,        0     ,      0    ,    15.0    ,    15.0   ,     15.0   ,     10.0     ,   11.0   ,     13.0   ,     13.0],
    [0     ,   20.0   ,     18.0     ,   18.0     ,      0      ,     0     ,    0    ,    5.0    ,    17.0     ,   13.0    ,    11.0   ,     11.0   ,     12.0],
    [0    ,    17.0   ,     15.0    ,    15.0     ,      0    ,       0    ,       0   ,        0    ,   14.0    ,    10.0    ,     8.0   ,     10.0    ,    11.0],
    [0    ,    12.0   ,     15.0   ,     13.0      ,    0     ,      0    ,       0    ,       0     ,    0     ,    6.0   ,      6.0   ,     11.0    ,    11.0],
    [0    ,    15.0  ,     13.0     ,   11.0      ,     0    ,       0     ,      0     ,      0    ,       0     ,      0   ,      1.0   ,       9.0  ,       9.0],
    [0    ,    15.0    ,    13.0    ,    11.0      ,     0    ,       0      ,     0    ,       0    ,       0       ,    0    ,       0   ,      8.0    ,     9.0],
    [0    ,    14.0     ,   10.0    ,    10.0      ,     0     ,      0      ,     0    ,       0     ,      0    ,       0      ,     0   ,        0   ,     1.0],
    [0   ,     13.0    ,     9.0    ,     9.0      ,     0      ,     0     ,      0     ,      0    ,       0    ,       0    ,       0     ,      0       ,    0]]

A = np.array([[1.0,16.0,11.0,13.0,15.0,14.0,11.0,12.0,15.0,13.0,12.0,13.0,13.0], 
    [0,17.0, 12.0, 14.0,16.0 , 15.0      ,  12.0     ,   13.0    ,    16.0 ,      14.0    ,    13.0   ,     14.0   ,     14.0],
    [0      ,     0    ,     7.0  ,       4.0    ,       0     ,      0     ,      0      ,     0    ,       0     ,      0     ,      0      ,     0     ,      0],
    [0     ,      0    ,       0  ,       3.0    ,       0      ,     0      ,     0      ,     0   ,        0      ,     0      ,     0    ,       0    ,       0],
    [0   ,     14.0    ,   10.0     ,    9.0   ,        0    ,     1.0    ,    16.0   ,     16.0     ,   16.0  ,      11.0    ,    12.0   ,     14.0     ,   14.0],
    [0    ,    13.0    ,     9.0     ,    8.0   ,        0     ,      0    ,    15.0    ,    15.0   ,     15.0   ,     10.0     ,   11.0   ,     13.0   ,     13.0],
    [0     ,   20.0   ,     18.0     ,   18.0     ,      0      ,     0     ,    0    ,    5.0    ,    17.0     ,   13.0    ,    11.0   ,     11.0   ,     12.0],
    [0    ,    17.0   ,     15.0    ,    15.0     ,      0    ,       0    ,       0   ,        0    ,   14.0    ,    10.0    ,     8.0   ,     10.0    ,    11.0],
    [0    ,    12.0   ,     15.0   ,     13.0      ,    0     ,      0    ,       0    ,       0     ,    0     ,    6.0   ,      6.0   ,     11.0    ,    11.0],
    [0    ,    15.0  ,     13.0     ,   11.0      ,     0    ,       0     ,      0     ,      0    ,       0     ,      0   ,      1.0   ,       9.0  ,       9.0],
    [0    ,    15.0    ,    13.0    ,    11.0      ,     0    ,       0      ,     0    ,       0    ,       0       ,    0    ,       0   ,      8.0    ,     9.0],
    [0    ,    14.0     ,   10.0    ,    10.0      ,     0     ,      0      ,     0    ,       0     ,      0    ,       0      ,     0   ,        0   ,     1.0],
    [0   ,     13.0    ,     9.0    ,     9.0      ,     0      ,     0     ,      0     ,      0    ,       0    ,       0    ,       0     ,      0       ,    0]]
) # Array of floats
print(A)
A = np.random.randint(0, 10, size=144).reshape(12, 12)
names = ['DQB1*02:02', 'DQB1*03:01' , 'DQB1*03:02' , 'DQB1*03:03' , 'DQB1*04:01' ,'DQB1*04:02',  'DQB1*05:01',  'DQB1*05:02',  'DQB1*06:01',  'DQB1*06:02',  'DQB1*06:03',  'DQB1*06:04',  'DQB1*06:09']
names2= ['DQB1*02:02', 'DQB1*03:01' , 'DQB1*03:02' , 'DQB1*03:03' , 'DQB1*04:01' ,'DQB1*04:02',  'DQB1*05:01',  'DQB1*05:02',  'DQB1*06:01',  'DQB1*06:02',  'DQB1*06:03',  'DQB1*06:04',  'DQB1*06:09']
df = pd.DataFrame(A, index=names, columns=names)
df.to_csv('df.csv', index=True, header=True, sep=' ')

clustermap = sb.clustermap(df)
plt.savefig('/Users/agathenaisadiguna/Downloads/clustermap.png')


N = np.array([[0, 1,	16,	11,	13,	15,	14,	11,	12,	15,	13,	12,	13,	13],
    [1,	0,	17,	12,	14,	16,	15,	12,	13,	16,	14,	13,	14,	14],
    [19, 20, 0,	7,	4,	15,	14,	18,	18,	13,	11,	10,	11,	11],
    [16,	17,	9,	0,	3,	13,	12,	18,	18,	18,	11,	10,	9,	9],
    [18,	19,	6,	3,	0,	12,	11,	18,	18,	16,	9,	8,	9,	9],
    [17,	18,	14,	10,	9	,0,	1,	16,	16,	16,	11,	12,	14,	14],
    [16,	17,	13,	9,	8,	1,	0,	15,	15,	15,	10	,11	,13,	13],
    [16,	17,	20,	18,	18,	19,	18,	0,	5,	17,	13,	11,	11,	12],
    [14,	15,	17,	15,	15,	16,	15,	2,	0,	14	,10,	8,	10,	11],
    [17,	18,	12,	15,	13,	16,	15,	14,	14,	0	,6,	6	,11,	11],
    [20,	21,	15,	13,	11,	16,	15,	15,	15,	11,	0,	1,	9,	9],
    [20,	21,	15,	13,	11,	18,	17,	14,	14,	12,	2,	0,	8,	9],
    [19,	20,	14,	10,	10,	18,	17,	12,	14,	15,	8,	6	,0,	1],
    [18,	19,	13,	9,	9,	17,	16,	12,	14,	14,	7,	6,	0,	0]])
N = np.random.randint(0, 10, size=196).reshape(14, 14)
names = ['DQB1*02:01',	'DQB1*02:02',	'DQB1*03:01',	'DQB1*03:02',	'DQB1*03:03',	'DQB1*04:01',	'DQB1*04:02',	'DQB1*05:01',	'DQB1*05:02',	'DQB1*06:01',	'DQB1*06:02',	'DQB1*06:03',	'DQB1*06:04',	'DQB1*06:09']
df2 = pd.DataFrame(N, index=names, columns=names)
df2.to_csv('df.csv', index=True, header=True, sep=' ')

clustermap = sb.clustermap(df2, cmap="vlag")
plt.savefig('/Users/agathenaisadiguna/Downloads/clustermap_finale.png')
