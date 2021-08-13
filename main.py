import csv
import pandas as pd
import numpy as np
# reading csv files
data =  pd.read_csv('movement_libras.data', sep=",")
# print(data)
# only for 
def preprocess_data(filename, has_names = False, has_index = False, columns = None, sep = ' '):
    with open(filename) as data_file:
        lines = data_file.readlines()

        # finding seperator
        if (' ' in lines[0]):
            sep = ' '
        elif (',' in lines[0]):
            sep = ','
        elif ('\t' in lines[0]):
            sep = '\t'
        else:
            print("Cannot identify a seperator: Please enter a seperator with the attribute 'sep' ")

        data_matrix = []
        for line in lines:
            data = line.strip().split(sep)
            data = [x for x in data if x != '']
            data_matrix.append(np.array(data))
        
        # checking for column headers        
        df = pd.DataFrame(np.array(data_matrix))
        df = df.apply(pd.to_numeric, errors='coerce')

        print(df)
        
        
        # checking if headers exist or not
        # if (not any(filter(lambda x: x.isnumeric(), headers))) or has_names:
        #     lines = lines[1:]
        # elif columns:
        #     headers = columns
        # else:
        #     column_heads = []
        #     for i in range(len(headers)):

        

preprocess_data('pop_failures.dat')

# with open('vowel.data.txt') as input_file:
#     lines = input_file.readlines()
#     newLines = []
#     for line in lines:
#         newLine = line.strip().split()
#         newLines.append( newLine )

# with open('output.csv', 'wb') as test_file:
#     file_writer = csv.writer(test_file)
#     file_writer.writerows( newLines )