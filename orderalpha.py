'''
To sort the alleles alphabetically in the columns of the table.
'''

# IMPORTS or LIBRARIES
import pandas as pd
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

# FUNCTION


def allele2alpha():
    dataframe = pd.read_excel(input)
    for i in range(0, len(dataframe), 1):
        j = 0
        while j < len(dataframe.iloc[0])-2:
            j += 1
            k = j+1
            value1 = str(dataframe.iloc[i][j])
            value2 = str(dataframe.iloc[i][k])
            list_values = [value1, value2]
            list_values.sort()
            dataframe.iat[i, j] = list_values[0]
            dataframe.iat[i, k] = list_values[1]
            j += 1
    dataframe.to_excel(output)


# MAIN


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-idir", "--inputdirectory")
    parser.add_argument("-o", "--output", help="Output file")
    args = vars(parser.parse_args())

    input = args["input"]
    inputdirectory = args["inputdirectory"]
    output = args["output"]

allele2alpha()
