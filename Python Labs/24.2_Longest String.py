"""
Write a program that takes in two strings and outputs the longest string.
If they are the same length then output the second string.

Ex. If the input is:

almond
pistachio

the output is:

pistachio


"""
a = str(input())
b = str(input())

if len(a) > len(b):
    print(a)
elif len(a) < len(b) or len(a) == len(b):
    print(b)