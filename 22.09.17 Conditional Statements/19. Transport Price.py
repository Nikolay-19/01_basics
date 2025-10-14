trip_distance = int(input())
time = str(input())

taxi = 0.7
taxi_day = 0.79
taxi_night = 0.9
bus = 0.09
train = 0.06

if trip_distance < 20:
    if time == "day":
        trip_cost = trip_distance * taxi_day + taxi
        print(f"{trip_cost:.2f}")
    if time == "night":
        trip_cost = trip_distance * taxi_night + taxi
        print(f"{trip_cost:.2f}")
if 20 <= trip_distance <100:
    trip_cost = trip_distance * bus
    print(f"{trip_cost:.2f}")
if trip_distance >= 100:
    trip_cost = trip_distance * train
    print(f"{trip_cost:.2f}")
    