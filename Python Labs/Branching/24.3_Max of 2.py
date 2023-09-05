"""
Write a program that takes in two integers and outputs the larger value.
If the two integers are the same, output the integers' value.

Ex: If the input is:

4
2

the output is:

4
"""
a = int(input())
b = int(input())

if a > b:
    print(a)
elif a < b or a ==b:
    print(b)
