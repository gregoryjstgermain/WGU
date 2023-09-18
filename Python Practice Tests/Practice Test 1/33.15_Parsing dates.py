"""
Write a program to read dates from input, one date per line.
Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored.
The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.

Hint: Use string[start:end] to get a substring when parsing the string and extracting the date.
Use the split() method to break the input into tokens.

Ex: If the input is:

March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1

then the output is:

3/1/1990
12/13/2003


"""

date = input()
all_dates = []

new_date = date.split('\n')
print(new_date)
