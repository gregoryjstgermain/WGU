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
       num_pennies, num_nickels, num_dimes, num_quarters = 0, 0, 0, 0
       return num_pennies, num_nickels, num_dimes, num_quarters
    if num > 0:
        total = num
        num_quarters = int(total / 25)
        new_total = total - (25 * num_quarters)
        num_dimes = int(new_total / 10)
        new_total = new_total - (10 * num_dimes)
        num_nickels = int(new_total / 5)
        num_pennies = new_total - (num_nickels * 5)

        #print(f'Pennies {num_pennies}')
        #print(f'Nickels {num_nickels}')
        #print(f'Dimes {num_dimes}')
        #print(f'Quarters {num_quarters}')

        return num_pennies, num_nickels, num_dimes, num_quarters


if __name__ == '__main__':
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    # Type your code here.

    if num_pennies == 1:
        print(f'{num_pennies} penny')
    elif num_pennies > 1:
        print(f'{num_pennies} pennies')
    if num_nickels == 1:
        print(f'{num_nickels} nickel')
    elif num_nickels > 1:
        print(f'{num_nickels} nickels')
    if num_dimes == 1:
        print(f'{num_dimes} dime')
    elif num_dimes > 1:
        print(f'{num_dimes} dimes')
    if num_quarters == 1:
        print(f'{num_quarters} quarter')
    elif num_quarters > 1:
        print(f'{num_quarters} quarters')
