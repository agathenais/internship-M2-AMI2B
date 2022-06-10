'''
To sort the alleles alphabetically in the columns of the table.
'''

# IMPORTS or LIBRARIES
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import io
import pandas as pd
import numpy as np


# FUNCTION


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


'''
def count3():
    # print(data['Epitopic charge'].tolist())

    list_allclass = [list_all_eplet]

    occurrences = {}
    # Checking the element from sample list present as key in dictionary
    # if yes than increment by 1 or create new key with value 1
    for i in list_allclass:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    # Printing dictionary
    # print("element count using dictionary", occurrences)

    # Printing all element with its count of Occurrence
    for key, value in occurrences.items():
        # print("{0} {1}".format(key, value))

        TESTDATA =
        # list_eplet + occurence
    df = (pd.read_csv(io.StringIO(TESTDATA), sep=" ")
          .to_csv(output_eplet_occurence))
'''

if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-dir", "--directory", help="directory")
    parser.add_argument("-ocs", "--output_convert_set", help='''
                        Output convert set where set() becomes empty_set and
                        predictions matches blank becomes it_match''')
    parser.add_argument("-oc", "--output_count", help='''Output count where
                        get count for each Epitopic charge''')
    parser.add_argument("-ocv2", "--output_countv2", help='''Output count
                        v2 where empty_set count 0 and it_match count No''')
    parser.add_argument("-oc2", "--output_count2", help=''' Output count2
                         where calculate every error number count''')

    args = vars(parser.parse_args())

    input = args["input"]
    directory = args["directory"]
    output_convert_set = args["output_convert_set"]
    output_count = args["output_count"]
    output_countv2 = args["output_countv2"]
    output_count2 = args["output_count2"]

data = pd.read_excel(input)

convertset()

data2 = pd.read_excel(output_convert_set)
data2["Count"] = np.nan

count()

data3 = pd.read_excel(output_count)


replacesetandblank()

data4 = pd.read_excel(output_countv2)

count2()

# count3()
