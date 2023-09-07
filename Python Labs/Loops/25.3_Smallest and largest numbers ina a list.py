"""
Write a program that reads a list of integers into a list as long as the integers are greater than zero,
then outputs the smallest and largest integers in the list.

Ex: If the input is:

10
5
3
21
2
-6

the output is:

2 and 21

You can assume that the list of integers will have at least 2 values.

"""

user_input = 1
input_list = []

while 0 < user_input:
    user_input = int(input())
    if 0 < user_input:
        input_list.append(user_input)

print(f'{min(input_list)} and {max(input_list)}')