"""
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

(1) Prompt the user to input a food item name, price, and quantity. Output an itemized receipt. (Submit for 2 points)

Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

Enter food item name:
hot dog
Enter item price:
2.00
Enter item quantity:
5

RECEIPT
5 hot dog @ $2.00 = $10.00
Total cost: $10.00

(2) Extend the program to prompt the user for a second item. Output an itemized receipt. (Submit for 2 points, so 4 points total)

Enter food item name:
hot dog
Enter item price:
2.00
Enter item quantity:
5

RECEIPT
5 hot dog @ $2.00 = $10.00
Total cost: $10.00


Enter second food item name:
ice cream
Enter item price:
2.50
Enter item quantity:
4

RECEIPT
5 hot dog @ $2.00 = $10.00
4 ice cream @ $2.50 = $10.00
Total cost: $20.00

(3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost. Output the total cost, the cost of gratuity, and the grand total. (Submit for 3 points, so 7 points total)

Enter food item name:
hot dog
Enter item price:
2.00
Enter item quantity:
5

RECEIPT
5 hot dog @ $2.00 = $10.00
Total cost: $10.00


Enter second food item name:
ice cream
Enter item price:
2.50
Enter item quantity:
4

RECEIPT
5 hot dog @ $2.00 = $10.00
4 ice cream @ $2.50 = $10.00
Total cost: $20.00

15% gratuity: $3.00
Total with tip: $23.00

"""

item_name = input('Enter food item name:\n')
item_price = input('Enter item price:\n')
item_quantity = int(input('Enter item quantity:\n'))
total_cost = item_price * item_quantity
print()
print(f'RECEIPT')
print(f'{item_quantity} {item_name} @ ${item_price:.2f} = ${total_cost:.2f}')
print(f'Total cost: ${total_cost:.2f}')
print()
second_item_name = input('Enter second food item name:\n')
second_item_price = input('Enter item price:\n')
second_item_quantity = int(input('Enter item quantity:\n'))
second_total_cost = second_item_price * second_item_quantity
new_total = float(total_cost + second_total_cost)
print()
print()
print(f'RECEIPT')
print(f'{item_quantity} {item_name} @ ${item_price:.2f} = ${total_cost:.2f}')
print(f'{second_item_quantity} {second_item_name} @ ${second_item_price:.2f} = ${second_total_cost:.2f}')
print(f'Total cost: ${new_total:.2f}')
print()
gratuity = float(0.15 * new_total)
total_with_gratuity = float(new_total + gratuity)
print(f'15% gratuity: ${gratuity:.2f}')
print(f'Total with tip: ${total_with_gratuity:.2f}')
# FIXME (1): Finish reading item price and quantity, then output a receipt

# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt

# FIXME (3): Add a gratuity and total with tip to the second receipt