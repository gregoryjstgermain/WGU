"""
Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:

4
3
2
1

where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels, and 1 is the number of pennies,
the output is:

Amount: $1.41

For simplicity, assume input is non-negative.

"""

quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())

total_q = quarters * 0.25
total_d = dimes * 0.10
total_n = nickels * 0.05
total_p = pennies * 0.01

total = total_q + total_d + total_n + total_p
print(f'Amount: ${total:.2f}')