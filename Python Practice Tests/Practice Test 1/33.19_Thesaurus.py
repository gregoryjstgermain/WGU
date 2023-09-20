"""
Given a set of text files containing synonyms for different words, complete the main program to output the synonyms for a
specific word. Each text file contains synonyms for the word specified in the file’s name, and each row within the file
lists the word’s synonyms that begin with the same letter, separated by a space. The program reads a word and a letter
from the user and opens the text file associated with the input word. The program then stores the contents of the
text file into a dictionary predefined in the program. Finally the program searches the dictionary and outputs
all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin
with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary.
Assume all letters are in lowercase.

Ex: If the input of the program is:

educate
c

the program opens the file educate.txt, which contains:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor

then the program outputs:

civilize
coach
cultivate

Ex: If the input of the program is:

educate
a

then the program outputs:

No synonyms for educate begin with a.


"""
synonyms = {}   # Define dictionary
s_word = input()
filename = s_word + ".txt"
synonym_letter = input()

#file1 = open(filename, "r")


with open(filename, 'r') as file1:
    lines = file1.readlines()
    for word in lines:
        key = word[0]
        words = word.split()
        synonyms[key] = words


if synonym_letter in synonyms:
    for i in synonyms[synonym_letter]:
        print(i)
else:
    print(f'No synonyms for {s_word} begin with {synonym_letter}.')
    #else:
     #   print(f'No synonyms for {word} begin with {synonym_letter}.')
