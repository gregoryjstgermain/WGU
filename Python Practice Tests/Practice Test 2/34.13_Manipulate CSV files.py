"""
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv".
Each file contains two rows of comma-separated values. Import the built-in module csv and use its open()
function and reader() method to create a dictionary of key:value pairs for each row of comma-separated
values in the specified file. Output the file contents as two dictionaries.

The solution output should be in the format

{'key': 'value', 'key': 'value', 'key': 'value'}
{'key': 'value', 'key': 'value', 'key': 'value'}

Sample Input/Output:

If the input is

input1.csv

then the expected output is

{'a': '100', 'b': '200', 'c': '300'}
{'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}

Alternatively, if the input is

input2.csv

then the expected output is

{'d': '400', 'e': '500', 'f': '600'}
{'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}

"""

#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements

import csv

#file = input()
file = 'input1.csv'

d1 = {}

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        row = [s.strip() for s in row]
        for i in range(0, len(row), 2):

            d1[row[i]] = row[i + 1]
        print(d1)
        d1 = {}






