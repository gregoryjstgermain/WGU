"""
Write the remove_evens() function, which receives a list of integers as a parameter and returns a new list of
integers containing only the odd numbers from the original list. The main program outputs values of the returned list.

Hint: If the original list has even numbers, then the new list will be smaller in length
than the original list and should have no blank elements.

Ex: If the list passed to the remove_evens() function is [1, 2, 3, 4, 5, 6, 7, 8, 9], then the
function returns and the program output is:

[1, 3, 5, 7, 9]

Ex: If the list passed to the remove_evens() function is [1, 9, 3], then the function returns and the program output is:

[1, 9, 3]


"""


def remove_evens(nums):
    new_nums = []
    for x in nums:
        if x % 2 != 0:
            new_nums.append(x)
    return new_nums

# Type your code here.

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_evens(nums)


    print(result)