"""
Write a program that removes all digits from the given input.

Ex: If the input is:

1244Crescent

the output is:

Crescent

The program must define and call the following function that takes a string as parameter and returns the
string without any digits.

def remove_digits(user_string)

"""


def remove_digits(user_string):
    new_string = ''
    for char in user_string:
        if not char.isdigit():
            new_string = new_string + char

    return new_string
# Type your code here.


if __name__ == '__main__':
# Type your code here.

    user_string = input()
    print(remove_digits(user_string))