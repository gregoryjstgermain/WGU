"""
Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.

the output is:

21

"""

user_text = str(input())
count = 0
length = len(user_text)

for x in user_text[0:0:1]:
    while x != " " and x != "," and x != "." and x !="!":
        count += 1


print(count)
