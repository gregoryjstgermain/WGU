"""
Write a function max_magnitude() with three integer parameters that returns the largest magnitude value.
Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

Ex: If the inputs are:

5
7
9

function max_magnitude() returns and the main program outputs:

9

Ex: If the inputs are:

-17
-8
-2

function max_magnitude() returns and the main program outputs:

-17

Note: The function does not just return the largest value, which for -17 -8 -2 would be -2.
Though not necessary, you may use the built-in absolute value function to determine the max magnitude,
but you must still output the input number (Ex: Output -17, not 17).

Your program must define and call the following function:
def max_magnitude(user_val1, user_val2, user_val3)

"""

def max_magnitude(user_val1, user_val2, user_val3):
    val1 = abs(user_val1)
    val2 = abs(user_val2)
    val3 = abs(user_val3)

    vals = [val1, val2, val3]

    max_val = max(vals)

    if max_val == val1:
        print(user_val1)
        return user_val1
    elif max_val == val2:
        print(user_val2)
        return user_val2
    elif max_val == val3:
        print(user_val3)
        return user_val3

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())


    max_magnitude(user_val1, user_val2, user_val3)