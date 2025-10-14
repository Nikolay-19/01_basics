import math

current_record = float(input())
distance = float(input())
speed = float(input())

resistance = math.floor(distance / 15) * 12.5
time = distance * speed + resistance

if current_record <= time:
    diff = time - current_record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
    