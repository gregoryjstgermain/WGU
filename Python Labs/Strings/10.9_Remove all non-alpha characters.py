"""
Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:

-Hello, 1 world$!

the output is:

Helloworld


"""

phrase = input()
new_phrase = ''

for x in phrase:
    if x.isalpha():
        new_phrase += x

print(new_phrase)