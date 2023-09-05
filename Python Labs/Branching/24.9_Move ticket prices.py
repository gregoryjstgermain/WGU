"""
Write a program that takes in a string that holds the values "day" or "night" and an integer that holds a person's age,
and outputs a movie ticket price. Movie prices are free for everyone under the age of 4.
Daytime prices are $8 for everyone age 4 or higher. Nighttime prices are $12 for ages 4 - 16, $15 for ages 17 - 54
and $13 for ages 55 and above.

Ex: If the input is:

night
50

the output is:

$15

Ex: If the input is:

day
15

the output is:

$8

Ex: If the input is:

night
3

the output is:

free


"""

time = str(input())
age = int(input())

if age <= 3:
    print("free")
elif time == "day" and 4 <= age:
    print("$8")
if time == "night":
    if 4 <= age <= 16:
        print("$12")
    elif 17 <= age <= 54:
        print("$15")
    elif 55 <= age:
        print("$13")