"""
Define a function called exact_change that takes the total change amount in cents and calculates the change
using the fewest coins. The coin types are pennies, nickels, dimes, and quarters.
Then write a main program that reads the total change amount as an integer input, calls exact_change(),
and outputs the change, one coin type per line. Use singular and plural coin names as appropriate, like
1 penny vs. 2 pennies. Output "no change" if the input is 0 or less.

Ex: If the input is:

0

(or less), the output is:

no change

Ex: If the input is:

45

the output is:

2 dimes
1 quarter

Your program must define and call the following function. The function exact_change() should return num_pennies, num_nickels, num_dimes, and num_quarters.
def exact_change(user_total)

"""
# Define your function here

def exact_change(num):
    if num <= 0:
        print('no change')
    elif num > 0:
        total = num


if __name__ == '__main__':
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    # Type your code here.
