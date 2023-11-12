"""
Create a solution that accepts a string input representing a grocery store item and an integer input
identifying the number of items purchased on a recent visit. The following dictionary purchase lists
available items as the key with the cost per item as the value.

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

Additionally,

    If fewer than ten items are purchased, the price is the full cost per item.
    If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
    If twenty-one or more items are purchased, the purchase gets a 10% discount.

Output the chosen item and total cost of the purchase to two decimal places.

The solution output should be in the format

item_purchased $total_purchase_cost

Sample Input/Output:

If the input is

bananas
12

then the expected output is

bananas $21.09

Alternatively, if the input is

cookies
144

then the expected output is

cookies $585.79

"""
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

items = str(input())
num_items = int(input())
total = purchase[items] * num_items

disc_5 = total - (0.05 * total)
disc_10 = total - (0.10 * total)

if num_items < 10:
    print(f'{items} ${total:.2f}')
elif 10 <= num_items <= 20:
    print(f'{items} ${disc_5:.2f}')
elif 21 < num_items:
    print(f'{items} ${disc_10:.2f}')

