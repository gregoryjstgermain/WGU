"""
Task:

Create a solution that accepts three integer inputs representing the number of times an employee travels to a
job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the
job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the
job site:

    Employee A: 15.62 miles
    Employee B: 41.85 miles
    Employee C: 32.67 miles

The solution output should be in the format

Distance: total_miles_traveled

Sample Input/Output:

If the input is

1
2
3

then the expected output is

Distance: 197.33 miles

"""

#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

num_a = int(input())
num_b = int(input())
num_c = int(input())

a_dist = 15.62
b_dist = 41.85
c_dist = 32.67

total_distance = (a_dist * num_a) + (b_dist * num_b) + (c_dist * num_c)

print(f'Distance: {total_distance:.2f} miles')
