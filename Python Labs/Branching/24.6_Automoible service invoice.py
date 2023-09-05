"""
(1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)

Ex:

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12



(2) Prompt the user for two services from the menu. (2 pts)

Ex:

Select first service:
Oil change
Select second service:
Car wax



(3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)

Davy's auto shop invoice

Service 1: Oil change, $35
Service 2: Car wax, $12

Total: $47



(4) Extend the program to allow the user to enter a dash (-), which indicates no service. (3 pts)

Ex:

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12

Select first service:
Tire rotation
Select second service:
-

Davy's auto shop invoice

Service 1: Tire rotation, $19
Service 2: No service

Total: $19

"""
oil_change = "Oil change"
tire_rotation = "Tire rotation"
car_wash = "Car wash"
car_wax = "Car wax"

cost_OC = int(35)
cost_TR = int(19)
cost_CW = int(7)
cost_CWX = int(12)

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

request1 = str(input("\nSelect first service:\n"))
request2 = str(input("Select second service:\n"))

print("\nDavy's auto shop invoice\n")
service_cost1 = 0
service_cost2 = 0
if request1 == oil_change:
    service_cost1 = cost_OC
    print(f'Service 1: {oil_change}, ${cost_OC}')
elif request1 == tire_rotation:
    service_cost1 = cost_TR
    print(f'Service 1: {tire_rotation}, ${cost_TR}')
elif request1== car_wash:
    service_cost1 = cost_CW
    print(f'Service 1: {car_wash}, ${cost_CW}')
elif request1 == car_wax:
    service_cost1 = cost_CWX
    print(f'Service 1: {car_wax}, ${cost_CWX}')
elif request1 == "-":
    service_cost1 = 0
    print(f'Service 1: No service')

if request2 == oil_change:
    service_cost2 = cost_OC
    print(f'Service 2: {oil_change}, ${cost_OC}')
elif request2 == tire_rotation:
    service_cost2 = cost_TR
    print(f'Service 2: {tire_rotation}, ${cost_TR}')
elif request2== car_wash:
    service_cost2 = cost_CW
    print(f'Service 2: {car_wash}, ${cost_CW}')
elif request2 == car_wax:
    service_cost2 = cost_CWX
    print(f'Service 2: {car_wax}, ${cost_CWX}')
elif request2 == "-":
    service_cost2 = 0
    print(f'Service 2: No service')

total_cost = int(service_cost1 + service_cost2)
print(f"\nTotal: ${total_cost}")