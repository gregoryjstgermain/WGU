"""
(1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)

Ex: If the input is:

yellow
Daisy
6

the output after the prompts is:

You entered: yellow Daisy 6

Note: User input is not part of the program output.

(2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).

Ex: If the input is:

yellow
Daisy
6

the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6


(3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).

Ex: If the input is:

yellow
Daisy
6

the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8


"""

# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = input('Enter favorite number:')
print(f'You entered: {favorite_color} {favorite_flower} {favorite_number}\n')

password1 = favorite_color + '_' + favorite_flower
password2 = favorite_number + favorite_color + favorite_number

print(f'First password: {password1}')
print(f'Second password: {password2}\n')

print(f'Number of characters in {password1}: {len(password1)}')
print(f'Number of characters in {password2}: {len(password2)}')

# FIXME (2): Output two password options



# FIXME (3): Output the length of the two password options