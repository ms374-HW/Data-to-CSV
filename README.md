# Data to CSV
A program that converts text files (.data / .dat) to CSV files. Done by Megha Sharma

# Contribution
1. Detecting indexes and column names
2. Custom settings for conversion

# Requirements
1. Numpy
2. Pandas
3. Python 3.7

# Getting Started
```
$ git clone https://github.com/ms374-HW/Data-to-CSV.git
$ cd Data-to-CSV
$ python3.7 main.py --file example_file.data
```
# Getting Help
```
$ python3.7 main.py --help
```
```
usage: main.py [-h] [--file FILE] [--has_names HAS_NAMES]
               [--index_at INDEX_AT] [--columns COLUMNS] [--sep SEP]
               [--save_path SAVE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           The path of the file
  --has_names HAS_NAMES
                        If data file already has names of the columns in the
                        first line
  --index_at INDEX_AT   Specifies the column names of the indices in the
                        dataset, can have one column or a list of columns
  --columns COLUMNS     Specifies the column names if not given in the data
                        file
  --sep SEP             Specifies the seperator between the columns in a
                        single line in the dataset
  --save_path SAVE_PATH
                        Specifies the path to save the CSV file to
```


