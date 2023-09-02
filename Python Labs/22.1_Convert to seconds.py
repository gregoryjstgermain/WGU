#Write a program that reads in hours, minutes, and seconds as input and outputs the time in seconds only
#Example input:
#1
#6
#40
#Output:
#Seocnds: 400

hours = int(input())
minutes = int(input())
seconds = int(input())

converted = (hours * 3600) + (minutes * 60) + seconds

print(f'Seconds: {converted}')
