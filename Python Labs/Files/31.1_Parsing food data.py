"""
Given a text file containing the availability of food items, write a program that reads the information from the
text file and outputs the available food items. The program first reads the name of the text file from the user.
The program then reads the text file, stores the information into four separate lists,
and outputs the available food items in the following format: name (category) -- description

Assume the text file contains the category, name, description, and availability of at least one food item,
separated by a tab character ('\t').

Ex: If the input of the program is:

food.txt

and the contents of food.txt are:

Sandwiches    Ham sandwich    Classic ham sandwich    Available
Sandwiches    Chicken salad sandwich  Chicken salad sandwich  Not available
Sandwiches    Cheeseburger    Classic cheeseburger    Not available
Salads    Caesar salad    Chunks of romaine heart lettuce dressed with lemon juice    Available
Salads    Asian salad Mixed greens with ginger dressing, sprinkled with sesame    Not available
Beverages    Water   16oz bottled water  Available
Beverages    Coca-Cola   16oz Coca-Cola  Not available
Mexican food    Chicken tacos   Grilled chicken breast in freshly made tortillas    Not available
Mexican food    Beef tacos  Ground beef in freshly made tortillas   Available
Vegetarian    Avocado sandwich    Sliced avocado with fruity spread   Not available

the output of the program is:

Ham sandwich (Sandwiches) -- Classic ham sandwich
Caesar salad (Salads) -- Chunks of romaine heart lettuce dressed with lemon juice
Water (Beverages) -- 16oz bottled water
Beef tacos (Mexican food) -- Ground beef in freshly made tortillas


"""

#file1 = open("food.txt", "r")

#print(file1.read())
#import re

filename = input()

file1 = open(filename, "r")
#contents = file1.read()
lines = file1.readlines()
for i in lines:
    if "Available" in i:
        i = str(i)
        a = i.strip()
        b = a.split('\t')
        #c = a.split('\t')


        #d = c.replace("Available")
        print(b)
        print(b[1], f'({b[0]}) -- {b[2]}')
        #print(c[1], f'({c[0]}) -- {c[2]}')
        #print(i)




file1.close()