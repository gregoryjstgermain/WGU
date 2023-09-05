"""
Write a program that takes in three lowercase characters and outputs the characters in alphabetical order.

Hint: Ordering three characters takes six permutations.

Ex: If the input is:

c
a
b

the output is:

a b c


"""
a = str(input())
b = str(input())
c = str(input())

ls = [a, b, c]
ls_ordered = ls.sort()
print(f'{ls[0]} {ls[1]} {ls[2]}')