"""
Write a program that takes in three integers as inputs and outputs the largest value.
Use a try block to perform all the statements. Use an except block to catch any EOFErrors caused by missing inputs,
output the number of inputs read, and output the largest value or "No max" if no inputs are read.

Note: Because inputs are pre-entered when running a program in the zyLabs environment,
the system throws the EOFError when inputs are missing. Test the program by running the program in the Develop mode.

Hint: Use a counter to keep track of the number of inputs read and compare the inputs
accordingly in the except block when an exception is caught.

Ex: If the input is:

3
7
5

the output is:

7

Ex: If the input is:

3

the system throws the EOFError and outputs:

1 input(s) read:
Max is 3

Ex: If no inputs are entered:


the system throws the EOFError and outputs:

0 input(s) read:
No max


"""
i = 0
try:

    num1 = input()
    i += 1
    num2 = input()
    i += 1
    num3 = input()
    i += 1

    if i == 2:
        print(f'{i} input(s) read:')
        print('Max is', max(num1, num2))
    elif i == 3:
        print(max(num1, num2, num3))

except EOFError:
    if i == 0:
        print(f'{i} input(s) read:')
        print('No max')
    elif i == 1:
        print(f'{i} input(s) read:')
        print('Max is', num1)





