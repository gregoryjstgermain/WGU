"""
Complete the reverse_list() function that returns a new string list containing all contents in the parameter
but in reverse order.

Ex: If the input list is:

['a', 'b', 'c']

then the returned list will be:

['c', 'b', 'a']

Note: Use a for loop. DO NOT use reverse() or reversed().

"""


def reverse_list(letters):
    letters = letters[::-1]
    return letters

# Type your code here.

if __name__ == '__main__':
    ch = ['a', 'b', 'c']
    print(reverse_list(ch))  # Should print ['c', 'b', 'a']