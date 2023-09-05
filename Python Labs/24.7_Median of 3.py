"""
Write a program that takes in three integers and outputs the median value (not the largest or smallest value).

Ex: If the input is:

7
1
4

the output is:

4


"""

import statistics

item1 = int(input())
item2 = int(input())
item3 = int(input())
items = [item1, item2, item3]
median = statistics.median(items)

print(median)