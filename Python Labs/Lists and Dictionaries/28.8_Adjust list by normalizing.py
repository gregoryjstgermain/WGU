"""
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data.
This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.

For this program, read in a list of floats and adjust their values by dividing all values by the largest value.
Output each value with two digits after the decimal point. Follow each number output by a space.

Ex: If the input is:

30.0 50.0 10.0 100.0 65.0

the output is:

0.30 0.50 0.10 1.00 0.65


"""
nums = input().split()
max_num = float(max(nums))
norm_nums = []
for x in nums:
    a = float(x) / max_num
    norm_nums.append(a)

toStr = ' '.join([str(elem) for elem in norm_nums])
print(toStr)
#print(f'{norm_nums[0]:.2f} {norm_nums[1]:.2f} {norm_nums[2]:.2f} {norm_nums[3]:.2f} {norm_nums[4]:.2f} ')
