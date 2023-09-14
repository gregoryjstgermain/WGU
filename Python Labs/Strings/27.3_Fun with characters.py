"""
Complete the check_character() function which has 2 parameters: A string, and a specified index.
The function checks the character at the specified index of the string parameter, and returns a string based on
the type of character at that location indicating if the character is a letter, digit, whitespace, or unknown character.

Ex: The function calls below with the given arguments will return the following strings:

check_character('happy birthday', 2) returns "Character 'p' is a letter"
check_character('happy birthday', 5) returns "Character ' ' is a white space"
check_character('happy birthday 2 you', 15) returns "Character '2' is a digit"
check_character('happy birthday!', 14) returns "Character '!' is unknown"

"""


def check_character(word, index):
    phrase = str()

    if index <= len(word):
        if word[index].isalpha():
            phrase = "Character '" + word[index] + "' is a letter"
            return phrase
        elif word[index].isdigit():
            phrase = "Character '" + word[index] + "' is a digit"
            return phrase
        elif word[index] == ' ':
            phrase = "Character '" + word[index] + "' is a white space"
            return phrase
        elif not word[index].isalpha():
            phrase = "Character '" + word[index] + "' is unknown"
            return phrase

# Type your code here.

if __name__ == '__main__':
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))