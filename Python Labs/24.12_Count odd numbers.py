"""
Write a program that takes in four positive integers and outputs the number of odd numbers.
(Hint: use the modulo operator to determine if a number is odd)

Ex: If the input is:

1
2
3
4

the output is:

2

Ex: If the input is:

19
19
19
19

"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

total = 0

if num1 % 2 != 0:
    total += 1
if num2 % 2 != 0:
    total += 1
if num3 % 2 != 0:
    total += 1
if num4 % 2 != 0:
    total += 1

print(total)