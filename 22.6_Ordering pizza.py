"""
A local pizza shop is selling a large pizza for $9.99. Given the number of pizzas to order as input,
output the subtotal for the pizzas, and then output the total after applying a sales tax of 6%.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Subtotal: ${yourValue:.2f}')

Ex: If the input is:

3

the output is:

Subtotal: $29.97
Total due: $31.77


"""

num_pizzas = int(input())
cost_per_pizza = 9.99
tax = float((num_pizzas * cost_per_pizza)) * 0.06
subtotal = float(num_pizzas * cost_per_pizza)
total_cost = float(subtotal + tax)

print(f'Subtotal: ${subtotal:.2f}')
print(f'Total due: ${total_cost:.2f}')