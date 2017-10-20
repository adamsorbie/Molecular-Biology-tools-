import pandas as pd
import sys

input_file = raw_input("Enter filename: ")
if ".csv" not in input_file:
    print("Error, this script accepts csv files only")
else:
    otu_table = pd.read_csv(input_file, sep=',', index_col=0)
    transpose = otu_table.transpose()
    output_file = raw_input("Enter output filename: ")
    transpose.to_csv(output_file, sep=',', encoding='utf-8')
sys.exit()
