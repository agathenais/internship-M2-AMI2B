from cgitb import reset
from lib2to3.pgen2.pgen import DFAState
import datacache
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import io 
import pprint

def convertset():
    #data['Epitopic charge'].loc[data['Donor epitope'] == data['Recipient epitope']] = " "
    #data['Epitopic charge'].loc[data['Donor epitope'] != data['Recipient epitope']] = "set()"
    #print(data.to_csv('/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/Travail_haplostats/fauxneg/haplostats_fauxneg_all3.csv'))
    for nrow in range(len(data['Epitopic charge'])):
        if str(data['Epitopic charge'][nrow]) == "set()":
            if data['Donor epitope'][nrow] == data['Recipient epitope'][nrow]:
                data['Epitopic charge'][nrow] = ' '
    data.to_excel('/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/EasyHLA FR/fauxnegvrai/easyhlfr_fauxnegvrai_DQB1_1.xlsx')     



def count():
    for i in data['Epitopic charge']:
        count = i.count(",")+1
        print(count)

def count2():
    data['Count'].value_counts().to_csv("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/EasyHLA FR/fauxnegvrai/easyhlfr_fauxnegvrai_DQB1_count2.csv")
       
from itertools import chain
def count3():
    #print(data['Epitopic charge'].tolist())
    
    list_allclass = ['181T', '78Y', '96Y', '104AK', '71E', '108P', 'rq74AV', '57DA', '37YV', '37Y', '112H', '28D', '31FY', '70DA', '4R', '16H', '38V', 'rq37YV', '58AY', '77TY', '70D', '86V', '98E', '32Y', '47YR', '85VV', '58A', 'rp67IE', '104A', '189R', 'rq75VT', '47Y', '73A', '74A', '140TV', '31F', '26F', '57D']
    
    
    occurrences = {}
    # Checking the element from sample list present as key in dictionary
    # if yes than increment by 1 or create new key with value 1
    for i in list_allclass:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    # Printing dictionary
    #print("element count using dictionary", occurrences)
    
    # Printing all element with its count of Occurrence
    for key,value in occurrences.items():
        #print("{0} {1}".format(key, value))
        
        TESTDATA = '''
181T 39
'''
    df = pd.read_csv(io.StringIO(TESTDATA), sep=" ").to_csv("/Users/agathenaisadiguna/Downloads/Stage M2/Travail haplostats EURCAU/haplostats_eurcau_locusDRB1_count3.csv")   


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class = ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",help="input file")
    parser.add_argument("-o", "--output",help="Output file")
    args = vars(parser.parse_args())

    input = args["input"]
    output = args["output"]

    #data = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/Travail HaploSFHI/eplet_dataHaplosfhi_fauxpos/table_graph_haplosfhi_v4/haplosfhi_all.xlsx")
    data = pd.read_excel("/Users/agathenaisadiguna/Downloads/Stage M2/calculsansblanc/EasyHLA FR/fauxnegvrai/easyhlfr_fauxnegvrai_DQB1_count.xlsx")

#convertset()
#count()
count2()
#count3()