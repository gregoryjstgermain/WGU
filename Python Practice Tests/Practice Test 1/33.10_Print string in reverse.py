"""
Write a program that takes in a line of text as input, and outputs that line of text in reverse.
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done

then the output is:

ereht olleH
yeH


"""
userinput = str(input())
stop = ['Done', 'done', 'd']

while userinput not in stop:
    print(userinput[::-1])
    userinput = str(input())

#print(phrase_reversed)
