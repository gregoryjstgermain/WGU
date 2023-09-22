"""
Write a program that first gets integers from input. The input begins with a threshold value.
Then, subsequent input values are added to a list until -1 is entered. Finally, output all integers less than or
equal to the threshold value.

Ex: If the input is:

100
50
60
140
200
75
-1

the output is:

50
60
75

The 100 indicates that the program should output all integers less than or equal to 100.
Next, five integers are added to the list: 50, 60, 140, 200, and 75. Finally, -1 indicates the end of the list.

Such functionality is common on sites like Amazon, where a user can filter results.

Write your code to define and use two functions:
get_user_values(nums)
output_ints_less_than_or_equal_to_threshold(nums, threshold)

"""
# Define your get_user_values function here


# Define your output_ints_less_than_or_equal_to_threshold function here
def get_user_values(nums):
    user_nums = int()

    while user_nums != -1:
        user_nums = int(input())
        nums.append(user_nums)

    #print(nums)
    return nums

def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    for x in nums:
        if x <= threshold and x != -1:
            print(x)
    #print()

if __name__ == '__main__':
    threshold = int(input())
    nums = []

    get_user_values(nums)
    output_ints_less_than_or_equal_to_threshold(nums, threshold)