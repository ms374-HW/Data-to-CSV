import pandas as pd
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file', default = '', help = 'The path of the file', type = str)
parser.add_argument('--has_names', default = False, help = 'If data file already has names of the columns in the first line', type = bool)
parser.add_argument('--index_at', default = None, help = 'Specifies the column names of the indices in the dataset, can have one column or a list of columns')
parser.add_argument('--columns', default = None, help = 'Specifies the column names if not given in the data file')
parser.add_argument('--sep', default = ' ', help = 'Specifies the seperator between the columns in a single line in the dataset', type = str)
parser.add_argument('--save_path', default = '', help = 'Specifies the path to save the CSV file to', type = str)


args = parser.parse_args()

filename = args.file
has_names = args.has_names
index_at = args.index_at
columns = args.columns
sep = args.sep
save_path = args.save_path



"""
    Program that preproceses a non CSV file in a text format (eg. .data, .dat files) and converts it into a 
    CSV file. The function is suitable for datasets with data in NUMERIC / REAL format. Any datasets with text or 
    other types might be incorrectly identified. If that is the case, special arguments are provided to ensure that 
    the user can flexibly choose the indices and columns
    Args:
        filename: The path of the file in a string (required)
        has_names: If data file already has names of the columns in the first line (default = False)
        index_at: Specifies the column names of the indices in the dataset, can have one column or a list of columns (default = None)
        columns: Specifies the column names if not given in the data file (default = None)
        sep: Specifies the seperator between the columns in a single line in the dataset (default = ' ')
    Returns:
        Does not return anything, instead creates a CSV file in the same directory for the dataset
"""

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

    # arrange the data as a matrix of rows and columns
    data_matrix = []
    for line in lines:
        data = line.strip().split(sep)
        data = [x for x in data if x != '']
        data_matrix.append(np.array(data))
    
    # finding the column names
    headers = None
    # if has names already
    if has_names:
        headers = data_matrix[0]
        data_matrix = data_matrix[1:]
    # if user specific column names
    elif columns:
        headers = columns
    
    # creating dataset
    df = pd.DataFrame(np.array(data_matrix), columns = headers)
    
    # to automatically find a column name list, we compare the first and second row to see if they have a different
    # dtype, which implies that the first row might be naming of the column 
    row_1 = pd.to_numeric(df.loc[0], errors = 'ignore')
    row_2 = pd.to_numeric(df.loc[1], errors = 'ignore')

    if any((map(lambda x,y: type(x) != type(y), row_1, row_2))):
        df.columns = df.iloc[0]
        headers = list(df.columns)
        df.drop(0, axis = 0, inplace = True)

    # converting all the dataframe values to numeric is possible
    df = df.apply(pd.to_numeric, errors='ignore')

    # checking indexes for the dataframe
    index_at = []
    for column in df.columns:
        if df[column].is_monotonic_increasing and df[column].dtype == np.int64 and len(df[column]) == len(set(df[column])):
            index_at.append(column)
    
    # setting indexes
    if index_at != []:
        df.set_index(index_at)
        df.drop(index_at, axis = 1, inplace = True)
    else:
        index_at = None

    if save_path == '':
        save_path = os.path.splitext(filename)[0] + '.csv'

    if not headers:
        headers = False

    df.to_csv(path_or_buf = save_path, header = headers, index_label = index_at)
    
