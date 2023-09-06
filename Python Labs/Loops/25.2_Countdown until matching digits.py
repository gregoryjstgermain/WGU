"""
Write a program that takes in an integer in the range 11-100 as input. The output is a countdown starting from the integer, and stopping when both output digits are identical.

Ex: If the input is:

93

the output is:

93
92
91
90
89
88

Ex: If the input is:

11

the output is:

11

Ex: If the input is:

9

or any value not between 11 and 100 (inclusive), the output is:

Input must be 11-100

Use a while loop. Compare the digits; do not write a large if-else for all possible same-digit numbers (11, 22, 33, …, 99),
as that approach would be cumbersome for larger ranges.

"""
user_input = int(input())

if 11 <= user_input <= 100:
    print(user_input)
    while user_input % 11 != 0:
        user_input -= 1
        print(user_input)
else:
    print("Input must be 11-100")