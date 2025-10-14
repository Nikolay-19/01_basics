bus_pr = 200
truck_pr = 175
train_pr = 120
bus_freights = 0
truck_freights = 0
train_freights = 0
total_pr = 0
total_weight = 0
items = int(input())

for a in range(1, items + 1):
    weight = int(input())
    
    if weight <= 3:
        bus_freights += weight
        total_weight += weight
        price = weight * bus_pr
        total_pr += price
        
    if 3 < weight <= 11:
        truck_freights += weight
        total_weight += weight
        price = weight * truck_pr
        total_pr += price
        
    if weight >= 12:
        train_freights += weight
        total_weight += weight
        price = weight * train_pr
        total_pr += price
        
average_pr = total_pr / total_weight
average_bus = bus_freights / total_weight * 100
average_truck = truck_freights / total_weight * 100
average_train = train_freights / total_weight * 100

print(f"{average_pr:.2f}")
print(f"{average_bus:.2f}%")
print(f"{average_truck:.2f}%")
print(f"{average_train:.2f}%")
