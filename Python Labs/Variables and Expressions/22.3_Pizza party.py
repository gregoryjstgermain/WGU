"""

Given the number of people attending a pizza party, output the number of needed pizzas and total cost.
For the calculation, assume that people eat 2 slices on average and each pizza has 12 slices and costs $14.95.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Cost: ${cost:.2f}')

Hint: Use the ceil() function from the math module to round up the number of pizzas so that enough pizzas are ordered.

Ex: If the input is:

4

the output is:

Pizzas: 1
Cost: $14.95
"""

import math

num_people = int(input())
slices_per_pizza = 12
cost_per_pizza = 14.95
slices_per_person = 2

if num_people * slices_per_person < slices_per_pizza:
    total_pizzas = 1
elif num_people * slices_per_person > slices_per_pizza:
    if num_people % 2 == 0:
        total_pizzas = int(num_people * slices_per_person / slices_per_pizza)
    elif  num_people  % 2 != 0:
        total_pizzas = int(1 + num_people * slices_per_person / slices_per_pizza)
if num_people * slices_per_person < 1:
    total_pizzas = 0

total_cost = total_pizzas * cost_per_pizza

print("Pizzas:", total_pizzas)
print(f'Cost: ${total_cost:.2f}')