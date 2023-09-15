"""
Write a program that finds word differences between two sentences.
The input begins with the first sentence and the following input line is the second sentence.
Assume that the two sentences have the same number of words.

The program displays word pairs that differ between the two sentences. One pair is displayed per line.

Ex: If the input is:

Smaller cars get better gas mileage
Tiny cars get great fuel economy

then the output is:

Smaller Tiny
better great
gas fuel
mileage economy

Hint: Store each input line into a list of strings.

"""

phrase1 = input().split()
phrase2 = input().split()

for item in phrase1:
    if not item in phrase2:
        print(item)
for element in phrase2:
    if not element in phrase1:
        print(element)