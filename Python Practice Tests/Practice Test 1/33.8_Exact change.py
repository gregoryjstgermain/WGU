"""
Write a program with total change amount as an integer input, and output the change using the fewest coins,
one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0

(or less than 0), the output is:

No change

Ex: If the input is:

45

the output is:

1 Quarter
2 Dimes


"""
cents = int(input())

if cents == 0:
    print("No change")
elif 0 < cents:
    dollars = int(cents / 100)
    if dollars == 1:
        print(dollars, "Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")
    leftover = cents - (dollars * 100)
    quarters = int(leftover / 25)
    if quarters == 1:
        print(quarters, "Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")
    leftover = leftover - (quarters * 25)
    dimes = int(leftover / 10)
    if dimes == 1:
        print(dimes, "Dime")
    elif dimes > 1:
        print(dimes, "Dimes")
    leftover = leftover - (dimes * 10)
    nickels = int(leftover / 5)
    if nickels == 1:
        print(nickels, "Nickel")
    elif nickels > 1:
        print(nickels, "Nickels")
    leftover = leftover - (nickels * 5)
    pennies = leftover
    if pennies == 1:
        print(pennies, "Penny")
    elif pennies > 1:
        print(pennies, "Pennies")