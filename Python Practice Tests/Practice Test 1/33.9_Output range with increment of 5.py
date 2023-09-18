"""
Write a program whose input is two integers. Output the first integer and subsequent increments of 5
as long as the value is less than or equal to the second integer. End with a newline.

Ex: If the input is:

-15
10

the output is:

-15 -10 -5 0 5 10

Ex: If the second integer is less than the first as in:

20
5

the output is:

Second integer can't be less than the first.

For coding simplicity, output a space after every integer, including the last.

"""
bottom = int(input())
top = int(input())

#bottom = -10
#top = 15

if bottom <= top:
    num_range= []
    for x in range(bottom, top + 1, 5):
        num_range.append(x)
    print(' '.join(map(str, num_range)),end=" \n")
    print()
elif top < bottom:
    print("Second integer can't be less than the first.")