"""
Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method.
The file contains a list of words separated by commas. Your program should output the words and their frequencies
(the number of times each word appears in the file) without any duplicates.

Ex: If the input is:

input1.csv

and the contents of input1.csv are:

hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy

the output is:

hello 1
cat 2
man 2
hey 2
dog 2
boy 2
Hello 1
woman 1
Cat 1

"""

import csv
filename = input()
#filename = 'input1.csv'

word_list = []
with open(filename, 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=',')


    for line in file:
        for word in line:
            word_list.append(word)

    unique_words = sorted(set(word_list), key=word_list.index)

    for x in unique_words:
        print(x, word_list.count(x))