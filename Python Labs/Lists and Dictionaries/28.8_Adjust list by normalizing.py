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
a,b,c,d,e = input().split()
norm_nums = [a,b,c,d,e]
#sort_nums = sorted(nums)
new_nums = []
#print(sort_nums)
#print(max_num)

sort_nums = sorted(norm_nums)
max_num = float(max(sort_nums))
print(max_num)
print(sort_nums)

for x in sort_nums:
    a = float(x) / max_num
    new_nums.append(a)


toStr = ' '.join([str(elem) for elem in new_nums])
print(toStr)
#print(f'{norm_nums[0]:.2f} {norm_nums[1]:.2f} {norm_nums[2]:.2f} {norm_nums[3]:.2f} {norm_nums[4]:.2f} ')
