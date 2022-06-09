from mhcgnomes import dataframe_from_parsed_objects
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook

'''
def sort_two_str(str1: str, str2: str):
    return tuple(sorted((str1, str2)))

if __name__ == "__main__":
    file_train = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/Travail HaploSFHI/eplet_dataHaplosfhi/haplosfhi_pred.xlsx")
    print(sort_two_str(str(file_train['A1']), str(file_train['A2'])))
'''
dataframe = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/EasyHLA FR/fauxnegvrai/easyhlaFR_fauxnegvrai.xlsx")
for i in range(0,len(dataframe),1):
    j = 0
    while j < len(dataframe.iloc[0])-1:
        j += 1
        k = j+1 
        value1 = str(dataframe.iloc[i][j])
        value2 = str(dataframe.iloc[i][k])
        list_values = [value1,value2]
        list_values.sort()
        dataframe.iat[i,j] = list_values[0]
        dataframe.iat[i,k] = list_values[1]
        j += 1
dataframe.to_excel('/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/EasyHLA FR/fauxnegvrai/easyhlaFR_fauxnegvrai_alpha.xlsx')