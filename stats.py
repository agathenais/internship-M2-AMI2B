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
    for nrow in range(len(data['Epitopic charge'])):
        if str(data['Epitopic charge'][nrow]) == "set()":
            if data['Donor epitope'][nrow] == data['Recipient epitope'][nrow]:
                data['Epitopic charge'][nrow] = ' '
    data.to_excel('path_1.xlsx')     



def count():
    for i in data['Epitopic charge']:
        count = i.count(",")+1
        print(count)

def count2():
    data['Count'].value_counts().to_csv("path_count2.csv")
       
from itertools import chain
def count3():
    #print(data['Epitopic charge'].tolist())
    
    list_allclass = ['181T', '78Y', ...]
    
    
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
...
''''
    df = pd.read_csv(io.StringIO(TESTDATA), sep=" ").to_csv("path_count3.csv")   


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class = ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",help="input file")
    parser.add_argument("-o", "--output",help="Output file")
    args = vars(parser.parse_args())

    input = args["input"]
    output = args["output"]
    
    
    data = pd.read_excel("path.xlsx")

#convertset()
#count()
#count2()
#count3()
