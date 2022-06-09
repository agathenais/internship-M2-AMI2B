'''
To count the occurrence of prediction errors
'''

# IMPORTS or LIBRARIES
import pandas as pd
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

# FUNCTIONS


def count_allele():
    df = pd.read_excel(input)
    df.value_counts().to_excel(output1)
    df2 = pd.read_excel(output1)
    index_names = df2[df2[donorallele] == df2[recipientallele]].index
    df2.drop(index_names, inplace=True)
    df2.to_excel(output2)

# MAIN


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-idir", "--inputdirectory")
    parser.add_argument("-o1", "--output1", help="Output file")
    parser.add_argument("-o2", "--output2", help="Output file")
    parser.add_argument("-da", "--donorallele", help="Donor allele")
    parser.add_argument("-ra", "--recipientallele", help="Recipient allele")
    args = vars(parser.parse_args())

    input = args["input"]
    inputdirectory = args["inputdirectory"]
    output1 = args["output1"]
    output2 = args["output2"]
    donorallele = args["donorallele"]
    recipientallele = args["recipientallele"]

count_allele()
