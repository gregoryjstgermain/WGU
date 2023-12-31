"""
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

(1) Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade.
Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size.
(Submit for 2 points).

Note: This zyLab outputs a newline after each user-input prompt.
For convenience in the examples below, the user's input value is shown on the next line,
but such values don't actually appear as output when the program runs.

Enter amount of lemon juice (in cups):
2
Enter amount of water (in cups):
16
Enter amount of agave nectar (in cups):
2.5
How many servings does this make?
6

Lemonade ingredients - yields 6.00 servings
2.00 cup(s) lemon juice
16.00 cup(s) water
2.50 cup(s) agave nectar

(2) Prompt the user to specify the desired number of servings.
Adjust the amounts of each ingredient accordingly,
and then output the ingredients and serving size. (Submit for 4 points, so 6 points total).

How many servings would you like to make?
48

Lemonade ingredients - yields 48.00 servings
16.00 cup(s) lemon juice
128.00 cup(s) water
20.00 cup(s) agave nectar

(3) Convert the ingredient measurements from (2) to gallons.
Output the ingredients and serving size. Note: There are 16 cups in a gallon. (Submit for 2 points, so 8 points total).

Lemonade ingredients - yields 48.00 servings
1.00 gallon(s) lemon juice
8.00 gallon(s) water
1.25 gallon(s) agave nectar


"""
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_cups:.2f} cup(s) agave nectar')
print()
servings = int(input('How many servings would you like to make?\n'))
lemon_juice_cups = float(servings / 3)
water_cups = float(servings * (8/3))
agave_cups = float(servings / 2.4)
print()
print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_cups:.2f} cup(s) agave nectar')
print()
lemon_juice_gals = float(lemon_juice_cups / 16)
water_gals = float(water_cups / 16)
agave_gals = float(agave_cups / 16)

print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_juice_gals:.2f} gallon(s) lemon juice')
print(f'{water_gals:.2f} gallon(s) water')
print(f'{agave_gals:.2f} gallon(s) agave nectar')

# FIXME (1): Finish reading other items into variables, then output the three ingredients

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons
