"""
Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.

the output is:

21

"""

user_text = str(input())
count = 0

for x in user_text:
        if x == " ":
                count += 0
        elif x == ".":
                count += 0
        elif x == "!":
                count += 0
        elif x == ",":
                count += 0
        else:
                count += 1

print(count)
