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
date = input()
all_dates = []

new_date = date.split('\n')
print(new_date)

"""

s=0
d={'january':1,
   'february':2,
   'march':3,
   'april':4,
   'may':5,
   'june':6,
   'july':7,
   'august':8,
   'september':9,
   'october':10,
   'november':11,
   'december':12}
while s!='-1':
    s=input()
    if "," in s:
        s = s.split(",")
        ar = s[0].split(" ")
        if len(ar)<2:
            continue
        month, date = ar[0], ar[1]
        year = s[1].strip()
        if d.get(month.lower()):
            print("{}/{}/{}".format(d[month.lower()], date, year))

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format