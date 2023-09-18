"""
Given an integer representing a 10-digit phone number, output the area code, prefix,
and line number using the format (800) 555-1212.

Ex: If the input is:

8005551212

the output is:

(800) 555-1212

Hint: Use % to get the desired rightmost digits. Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.

Hint: Use // to shift right by the desired amount. Ex: Shifting 572 right by 2 digits is done by 572 // 100,
which yields 5. (Recall integer division discards the fraction).

For simplicity, assume any part starts with a non-zero digit. So 0119998888 is not allowed.

"""

phone_number = input()
print(f'({phone_number[0]}{phone_number[1]}{phone_number[2]}) {phone_number[3]}{phone_number[4]}{phone_number[5]}-{phone_number[6]}{phone_number[7]}{phone_number[8]}{phone_number[9]}')

