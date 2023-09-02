"""
The volume and area of a cylinder are calculated as:

    Volume = πr2h
    Area = 2πrh + 2πr2

Given the radius and height of a cylinder as floating-point numbers, output the volume and area of the cylinder.

Hint: Use the built-in pow() function and the constant pi from the math module in your calculations.

Output each floating-point value with one digit after the decimal point, which can be achieved as follows:
print(f'Volume: {yourValue:.1f} cubic inches')

Ex: If the input is:

5.2
8.1

where 5.2 is the radius of the cylinder and 8.1 is the height of the cylinder, then the output is:

Volume: 688.1 cubic inches
Surface area: 434.5 square inches


"""
import math

radius = float(input())
height = float(input())

volume = math.pi * (radius ** 2) * height
area = (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))

print(f'Volume: {volume:.1f} cubic inches')
print(f'Surface area: {area:.1f} square inches')
