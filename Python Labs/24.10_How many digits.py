"""
Write a program that inputs an integer (0 - 9999) and outputs the number of digits.

Ex: If the input is:

7493

the output is:

4 digits

Ex: If the input is:

7

the output is:

1 digit


"""
digits = str(input())

total_digits = len(digits)

if total_digits == 0:
    print(f'{total_digits} digits')
elif total_digits == 1:
    print(f'{total_digits} digit')
elif total_digits > 1:
    print(f'{total_digits} digits')
