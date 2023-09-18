"""
A palindrome is a word or a phrase that is the same when read both forward and backward.
Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob

the output is:

bob is a palindrome

Ex: If the input is:

bobby

the output is:

bobby is not a palindrome

Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

"""
phrase = input()
phrase_mod = phrase.replace(" ", "")
phrase_reversed = phrase_mod[::-1]


if phrase_mod == phrase_reversed:
    print(f'{phrase} is a palindrome')
elif phrase != phrase_reversed:
    print(f'{phrase} is not a palindrome')