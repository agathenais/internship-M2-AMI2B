'''
To sort the alleles alphabetically in the columns of the table.
'''

# IMPORTS or LIBRARIES
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import io
import pandas as pd
import numpy as np
import ast
import re


# FUNCTION

def str2list():
    for i in range(len(data0)):
        data0["Donor epitope"][i] = eval(data0["Donor epitope"][i])
        data0["Recipient epitope"][i] = eval(
            data0['Recipient epitope'][i])
    data0.to_excel(output_list)


def convertset():
    for nrow in range(len(data['Epitopic charge'])):
        if str(data['Epitopic charge'][nrow]) == "set()":
            if data['Donor epitope'][nrow] == data['Recipient epitope'][nrow]:
                data['Epitopic charge'][nrow] = 'it_match'
            else:
                data['Epitopic charge'][nrow] = 'empty_set'
    data.to_excel(output_convert_set)


def count():
    for i in range(len(data2['Epitopic charge'])):
        tmp_count = data2['Epitopic charge'][i].count(",")+1
        data2["Count"][i] = tmp_count
    data2.to_excel(output_count)


def replacesetandblank():
    for i in range(len(data3['Epitopic charge'])):
        if data3['Epitopic charge'].values[i] == "empty_set":
            data3['Count'].values[i] = "0"
        elif data3['Epitopic charge'][i] == "it_match":
            data3['Count'][i] = "No"
    data3.to_excel(output_countv2)


def count2():
    data4['Count'].value_counts().to_csv(output_count2)


def count3():
    list_allclass = data3['Epitopic charge'].tolist()
    out_list = ''.join(list_allclass)
    result = out_list.split("'")[1::2]

    occurrences = {}
    for i in result:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    pd.DataFrame({"eplet": occurrences.keys(), "occurrences": occurrences
                  .values()}).to_csv(output_eplet_occurence)


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-dir", "--directory", help="directory")
    parser.add_argument("-ol", "--output_list", help="str2list")
    parser.add_argument("-ocs", "--output_convert_set", help='''
                        Output convert set where set() becomes empty_set and
                        predictions matches blank becomes it_match''')
    parser.add_argument("-oc", "--output_count", help='''Output count where
                        get count for each Epitopic charge''')
    parser.add_argument("-ocv2", "--output_countv2", help='''Output count
                        v2 where empty_set count 0 and it_match count No''')
    parser.add_argument("-oc2", "--output_count2", help=''' Output count2
                         where calculate every error number count''')
    parser.add_argument("-os", "--output_stats", help=''' Output stats''')
    parser.add_argument("-oeo", "--output_eplet_occurence", help=''' Output
                        eplet occurence''')

    args = vars(parser.parse_args())

    input = args["input"]
    directory = args["directory"]
    output_list = args["output_list"]
    output_convert_set = args["output_convert_set"]
    output_count = args["output_count"]
    output_countv2 = args["output_countv2"]
    output_count2 = args["output_count2"]
    output_stats = args["output_stats"]
    output_eplet_occurence = args["output_eplet_occurence"]

data0 = pd.read_excel(input)

str2list()

data = pd.read_excel(output_list)

convertset()

data2 = pd.read_excel(output_convert_set)
data2["Count"] = np.nan

count()

data3 = pd.read_excel(output_count)


replacesetandblank()

data4 = pd.read_excel(output_countv2)

count2()

data5 = pd.read_csv(output_count2)

count3()
