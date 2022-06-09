"""
Compare eplets between donor and recipient
"""

# IMPORTS or LIBRARIES
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import pandas as pd
import os


# FUNCTIONS
def split_dataframe(df):
    donordf = df.filter(regex='_T')
    recipientdf = df.filter(regex='_P')
    return [donordf, recipientdf]


def allele_df_to_eplets_dict(df, patient_type, class_type, df_1, df_2, df_3):
    if class_type == 1:
        allele_list = ['A', 'B', 'C']
    else:
        allele_list = ['DP', 'DQ', 'DR']
    dict = {}
    for row in range(len(df[patient_type])):
        eplet_list = []
        for allele in df.columns[1:]:
            cell = str(df.at[row, allele])
            if allele_list[0] in cell:
                try:
                    (eplet_list.extend([x for x in df_1.loc[[cell]].values
                                        .flatten().tolist() if str(x)
                                        != 'nan']))
                except KeyError:
                    pass
            elif allele_list[1] in cell:
                try:
                    (eplet_list.extend([x for x in df_2.loc[[cell]].values
                                        .flatten().tolist() if str(x)
                                        != 'nan']))
                except KeyError:
                    pass
            elif allele_list[2] in cell:
                try:
                    (eplet_list.extend([x for x in df_3.loc[[cell]].values
                                        .flatten().tolist() if str(x)
                                        != 'nan']))
                except KeyError:
                    pass
            dict[df[patient_type].iloc[row]] = set(eplet_list)
    return dict


def donordict_to_dataframe(donordictunique):
    donordict_final = pd.DataFrame(list(dict(donordictunique).items()))
    return donordict_final


def recipientdict_to_dataframe(recipientdictunique):
    recipientdict_final = pd.DataFrame(list(dict(recipientdictunique).items()))
    return recipientdict_final


def row_wise_D_R_comparison(recipientdictunique, donordictunique):
    charge_epitopique = {}
    d = {}
    Rkeys_list = recipientdictunique.keys()
    DKeys_list = donordictunique.keys()
    for rkey, dkey in zip(Rkeys_list, DKeys_list):
        charge_epitopique = (set(donordictunique.get(dkey)).difference
                                (set(recipientdictunique.get(rkey))))
        d[str(rkey)+'vs'+str(dkey)] = charge_epitopique
    d2 = d.items()
    d3 = pd.DataFrame(d2)
    return d3


def eplet_cross_verification(d3):
    verified = {}
    for i, rows in d3.iterrows():
        d3.rename(columns={0: 'Truc'}, inplace=True)
        verified[str(d3['Truc'].iloc[i])] = []
        for eplet in rows[1]:
            if str(eplet) != 'None':
                if "_" in eplet:
                    eplet = eplet.split("_")[0]
                else:
                    eplet = eplet
                if str(data[eplet].loc[1]) == "Yes":
                    verified[str(d3['Truc'].iloc[i])].append(eplet)
    verified2 = verified.items()
    verified3 = pd.DataFrame(verified2)
    print(verified3)
    return verified3


def final_eplet_machin_to_csv(verified, donordict_final,
                              recipientdict_final, d3, verified3):
    if verified is not None:
        bestcol = ["Donor", "Donor epitope", "Recipient", "Recipient epitope",
                   "Donor vs recipient", "Epitopic charge",
                   "Donor vs recipient", "Epitopic charge verified"]
    else:
        bestcol = ["Donor", "Donor epitope", "Recipient", "Recipient epitope",
                   "Donor vs recipient", "Epitopic charge"]
    horizontal_concat = pd.concat([donordict_final, recipientdict_final,
                                   d3, verified3], axis=1)
    horizontal_concat.columns = bestcol
    horizontal_concat.to_csv(output)


def verified_column_only(verifiedonly, donordict_final, recipientdict_final,
                         verified3):
    if verifiedonly is not None:
        bestcol = ["Donor", "Donor epitope", "Recipient", "Recipient epitope",
                   "Donor vs recipient", "Epitopic charge verified"]
        horizontal_concat = pd.concat([donordict_final, recipientdict_final,
                                       verified3], axis=1)
        horizontal_concat.columns = bestcol
        horizontal_concat.to_csv(output)


# MAIN


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-idir", "--inputdirectory")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-c1", "--classI", help="Class I")
    parser.add_argument("-c2", "--classII", help="Class II")
    parser.add_argument("-v", "--verified", help="verified eplets")
    parser.add_argument("-vo", "--verifiedonly", help="verified column only")
    args = vars(parser.parse_args())

    input = args["input"]
    inputdirectory = args["inputdirectory"]
    output = args["output"]
    classI = args["classI"]
    classII = args["classII"]
    verified = args["verified"]
    verifiedonly = args["verifiedonly"]

    df = pd.read_excel(input)
    A = pd.read_csv(os.path.join(inputdirectory, "A.csv")).set_index("allele")
    B = pd.read_csv(os.path.join(inputdirectory, "B.csv")).set_index("allele")
    C = pd.read_csv(os.path.join(inputdirectory, "C.csv")).set_index("allele")
    DP = (pd.read_csv(os.path.join(inputdirectory, "DP.csv"))
          .set_index("allele"))
    DQ = (pd.read_csv(os.path.join(inputdirectory, "DQ.csv"))
          .set_index("allele"))
    DR = (pd.read_csv(os.path.join(inputdirectory, "DR.csv"))
          .set_index("allele"))
    data = pd.read_csv(os.path.join(inputdirectory, "ep_data.csv"))

    list_df = split_dataframe(df)
    donordf = list_df[0]
    recipientdf = list_df[1]

    if classI is not None and classII is None:
        donordictunique = allele_df_to_eplets_dict(donordf, 'ID_T', 1, A, B, C)
        recipientdictunique = allele_df_to_eplets_dict(recipientdf, 'ID_P',
                                                       1, A, B, C)

    if classII is not None and classI is None:
        donordictunique = allele_df_to_eplets_dict(donordf, 'ID_T', 2, DP, DQ,
                                                   DR)
        recipientdictunique = allele_df_to_eplets_dict(recipientdf, 'ID_P', 2,
                                                       DP, DQ, DR)

    if classI is not None and classII is not None:
        donordictunique = {}
        recipientdictunique = {}
        donordict = allele_df_to_eplets_dict(donordf, 'ID_T', 1, A, B, C)
        recipientdict = allele_df_to_eplets_dict(recipientdf, 'ID_P', 1, A, B,
                                                 C)
        donordict_2 = allele_df_to_eplets_dict(donordf, 'ID_T', 2, DP, DQ, DR)
        recipientdict_2 = allele_df_to_eplets_dict(recipientdf, 'ID_P', 2, DP,
                                                   DQ, DR)

        for key, value in donordict.items():
            donordictunique[key] = set()
        for key, value in donordict_2.items():
            donordictunique[key] = set()

        for key, value in donordict.items():
            for eplet in value:
                donordictunique[key].add(eplet+"_1")
        for key, value in donordict_2.items():
            for eplet in value:
                donordictunique[key].add(eplet+"_2")

        for key, value in recipientdict.items():
            recipientdictunique[key] = set()
        for key, value in recipientdict_2.items():
            recipientdictunique[key] = set()

        for key, value in recipientdict.items():
            for eplet in value:
                recipientdictunique[key].add(eplet+"_1")
        for key, value in recipientdict_2.items():
            for eplet in value:
                recipientdictunique[key].add(eplet+"_2")

    if verifiedonly is not None:

        donordict_final = donordict_to_dataframe(donordictunique)
        recipientdict_final = recipientdict_to_dataframe(recipientdictunique)
        d3 = row_wise_D_R_comparison(recipientdictunique, donordictunique)
        verified3 = eplet_cross_verification(d3)
        verified_column_only(verifiedonly, donordict_final,
                             recipientdict_final, verified3)
    else:
        donordict_final = donordict_to_dataframe(donordictunique)
        recipientdict_final = recipientdict_to_dataframe(recipientdictunique)
        d3 = row_wise_D_R_comparison(recipientdictunique, donordictunique)
        verified3 = eplet_cross_verification(d3)
        final_eplet_machin_to_csv(verified, donordict_final,
                                  recipientdict_final, d3, verified3)
