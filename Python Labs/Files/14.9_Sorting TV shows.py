"""
Write a program that first reads in the name of an input file and then reads the input file using the
file.readlines() method. The input file contains an unsorted list of number of seasons followed by the
corresponding TV show. Your program should put the contents of the input file into a dictionary where
the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could
have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt.
Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in
the input file. Next, sort the dictionary by values (alphabetical order), and output the results to a
file named output_titles.txt.

Ex: If the input is:

file1.txt

and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote

the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons

and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace

"""

# Type your code here
file = input() #user file input
with open(file) as f: #open file
    data = f.readlines()
dict_info = {}
for i in range(0, len(data)-1, 2):
    season = int(data[i].strip())
    name = data[i+1].strip()
    if(season in dict_info):
        dict_info[season].append(name)
    else:
        dict_info[season] = [name]

#OUTPUT KEYS
keys = list(dict_info.keys()) #will list the dictionary keys
keys.sort() #will sort the keys from min to max
with open('output_keys.txt', 'w') as f:
    for key in keys:
        names = '; '.join(name for name in dict_info[key]) #will print the name with number
        f.write(str(key)+': '+names+"\n")
names = [] #Dictionary value
for item in dict_info: #will add name to dict
    for name in dict_info[item]:
        names.append(name)

#OUTPUT TITTLE
names.sort() #sort names from min to max
with open('output_titles.txt', 'w') as f: #open the file
    for name in names: #will write name plus a new line
        f.write(name+'\n')