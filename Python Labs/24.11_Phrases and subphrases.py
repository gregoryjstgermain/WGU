"""
Write a program that reads two phrases on separate lines and outputs one of four responses:

1) Phrase one is found within phrase two

2) Phrase two is found within phrase one

3) Both phrases match

4) No matches

Hint: Use membership operator in.

Ex: If the input is:

fire
firetruck

the output is:

fire is found within firetruck

Ex: If the input is:

the green grass grows
green grass

the output is:

green grass is found within the green grass grows

Ex: If the input is:

pick a card
pick a card

the output is:

Both phrases match

Ex: If the input is:

apples
oranges

the output is:

No matches


"""

phrase1 = str(input())
phrase2 = str(input())

if phrase1 in phrase2 and phrase1 != phrase2:
    print(f'{phrase1} is found within {phrase2}')
elif phrase2 in phrase1 and phrase2 != phrase1:
    print(f'{phrase2} is found within {phrase1}')
elif phrase1 == phrase2:
    print("Both phrases match")
else:
    print("No matches")