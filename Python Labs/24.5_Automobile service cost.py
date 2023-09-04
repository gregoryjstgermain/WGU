"""
(1) Prompt the user for an automobile service. Output the user's input. (1 pt)

Ex:

Enter desired auto service:
Oil change
You entered: Oil change


(2) Output the price of the requested service. (4 pts)

Ex:

Enter desired auto service:
Oil change
You entered: Oil change
Cost of oil change: $35


The program should support the following services (all integers):

    Oil change -- $35
    Tire rotation -- $19
    Car wash -- $7

If the user enters a service that is not listed above, then output the following error message:

Error: Requested service is not recognized


"""
oil_change = "Oil change"
tire_rotation = "Tire rotation"
car_wash = "Car wash"

cost_OC = 35
cost_TR = 19
cost_CW = 7

request = str(input("Enter desired auto service:\n"))
print(f'You entered: {request}')
if request == oil_change:
    print(f'Cost of {oil_change.lower()}: ${cost_OC}')
elif request == tire_rotation:
    print(f'Cost of {tire_rotation.lower()}: ${cost_TR}')
elif request == car_wash:
    print(f'Cost of {car_wash.lower()}: ${cost_CW}')
elif request != oil_change or request != tire_rotation or request != car_wash:
    print("Error: Requested service is not recognized")