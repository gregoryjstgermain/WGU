"""
Write a program that reads a list of words. Then, the program outputs those words and their frequencies (case insensitive).

Ex: If the input is:

hey Hi Mark hi mark

the output is:

hey 1
Hi 2
Mark 2
hi 2
mark 2

Hint: Use lower() to set each word to lowercase before comparing.

"""

phrase = input()
lower_phrase = phrase.lower()
mod_phrase = phrase.split()
mod_lower_phrase = lower_phrase.split()

for word in mod_phrase:
    print(word, mod_lower_phrase.count(word.lower()))
