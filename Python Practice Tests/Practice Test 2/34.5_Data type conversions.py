"""
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting
the inputs to the requested data type prior to finding the sum.

    First output: sum of five inputs maintained as integer values
    Second output: sum of five inputs converted to float values
    Third output: sum of five inputs converted to string values (concatenate)

The solution output should be in the format

Integer: integer_sum_value
Float: float_sum_value
String: string_sum_value

Sample Input/Output:

If the input is

1
3
6
2
7

then the expected output is

Integer: 19
Float: 19.0
"""

#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

int_total = num1 +num2 + num3 + num4 + num5
float_total = float(num1 +num2 + num3 + num4 + num5)
str_total = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f'Integer: {int_total}')
print(f'Float: {float_total}')
print(f'String: {str_total}')