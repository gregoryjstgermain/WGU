"""
Write a recursive function called reverse_string() that takes in a string as parameter and returns the
string in reversed order. The main function is provided to read a string from the user and call the
reverse_string() function.

Ex: If the input of the program is:

Hello

the reverse_string() function returns and the program outputs:

Reverse of "Hello" is "olleH".

Ex: If the input of the program is:

Hello, world!

the reverse_string() function returns and the program outputs:

Reverse of "Hello, world!" is "!dlrow ,olleH".

Hint: Move the first character to the end of the returning string and pass the remaining sub-string to the
next reverse_string() function call.

"""

# TODO: Write recursive reverse_string() function here.

def reverse_string(str):
    print()


if __name__ == "__main__":
    in_str = input()
    result_str = reverse_string(in_str)
    print('Reverse of "' + in_str +  '" is "' + result_str + '".')