"""
A pedometer treats walking 2,000 steps as walking 1 mile. Write a steps_to_miles() function that takes the
number of steps as a parameter and returns the miles walked. The steps_to_miles() function throws a
ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function,
and outputs the returned value from the steps_to_miles() function. Use a try-except block to catch any ValueError
object thrown by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345

the output of the program is:

2.67

Ex: If the input of the program is:

-3850

the output of the program is:

Exception: Negative step count entered.


"""

# Define your method here

def steps_to_miles(steps):

    miles = steps / 2000
    if miles >= 0:

        print(f'{miles:.2f}')
        return miles
    else:
        raise ValueError



if __name__ == '__main__':
    # Type your code here.
    steps = int(input())
    #print(f'{steps_to_miles(steps):.2f}')
    try:
        steps_to_miles(steps)
    except ValueError:
        print("Exception: Negative step count entered.")


