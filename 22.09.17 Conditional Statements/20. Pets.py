import math
trip_time = int(input())
food_available = int(input())
day_dog = float(input())
day_cat = float(input())
day_turtle = float(input())

food_dog = trip_time * day_dog
food_cat = trip_time * day_cat
food_turtle = trip_time * day_turtle / 1000
total = food_dog + food_cat + food_turtle
food_left = abs(food_available - total)

if food_available >= total:
    print(f"{math.floor(food_left)} kilos of food left.")
if food_available < total:
    print(f"{math.ceil(food_left)} more kilos of food are needed.")
    