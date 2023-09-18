"""
Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of
gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

Ex: If the input is:

20.0
3.1599

where the gas mileage is 20.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:

3.16 11.85 79.00

Note: Real per-mile cost would also include maintenance and depreciation

Gas Cost = Distance / Miles per Gallon * Price Per Gallon
"""

mileage = float(input())
cost_per_gallon = float(input())

d1 = 20
d2 = 75
d3 = 500


cost1 = (d1 / mileage   ) * cost_per_gallon
cost2 = (d2 / mileage   ) * cost_per_gallon
cost3 = (d3 / mileage   ) * cost_per_gallon

print(f'{cost1:.2f} {cost2:.2f} {cost3:.2f}')

