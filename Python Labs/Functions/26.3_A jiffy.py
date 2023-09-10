"""
A "jiffy" is the scientific name for 1/100th of a second. Define a function named jiffies_to_seconds that takes
the number of "jiffies" as a parameter, and returns the number of seconds.
Then, write a main program that reads the number of jiffies (float) as an input, calls function jiffies_to_seconds()
with the input as argument, and outputs the number of seconds.

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

Ex: If the input is:

15.25

the output is:

0.152

The program must define and call the following function:
def jiffies_to_seconds(user_jiffies)

"""

def jiffies_to_seconds(user_jiffies):
    seconds = user_jiffies / 100
    print(f'{seconds:.3f}')
    return seconds

if __name__ == '__main__':
    user_jiffies = float(input())
    jiffies_to_seconds(user_jiffies)