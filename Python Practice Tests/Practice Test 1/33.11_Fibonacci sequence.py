"""
The Fibonacci sequence begins with 0 and then 1 follows.
All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function,
which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7

the output is:

fibonacci(7) is 13

Note: Use a for loop and DO NOT use recursion.

"""

def fibonacci(n):
    # Type your code here.
    sequence = [0, 1]
    n1, n2 = 0, 1
    count = 0
    num_terms = 100
    if n < 0:
        return -1
    while count < num_terms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        sequence.append(nth)

    #print(sequence)
    return sequence[n]

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')