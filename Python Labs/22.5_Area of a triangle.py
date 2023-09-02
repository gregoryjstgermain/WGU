import math

side1 = float(input())
side2 = float(input())
side3 = float(input())

s = 0.5 * (side1 + side2 + side3)
area = math.sqrt(s * (s-side1) * (s - side2) * (s - side3))

print(f'The area of the triangle is: {area:.3f}')