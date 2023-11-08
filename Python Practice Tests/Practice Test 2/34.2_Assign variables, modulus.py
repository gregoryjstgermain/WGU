"""
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same
format shown in the sample(s) below, including capitalization and whitespace.
Task:

Create a solution that accepts an integer input representing any number of ounces. Output the converted total
number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound
and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3

Sample Input/Output:

If the input is

32035

then the expected output is

Tons: 1
Pounds: 2
Ounces: 3

"""

total = int(input())

tons = int((total / 16) / 2000)
new_total = total - ((tons * 16) * 2000)
pounds = int(new_total / 16)
ounces = new_total - (pounds * 16)

print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {ounces}')

