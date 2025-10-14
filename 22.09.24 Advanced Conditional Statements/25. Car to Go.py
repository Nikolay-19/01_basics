budget = float(input())
season = str(input())

car_class = ""
body_type = ""
total = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        body_type = "Cabrio"
        total = budget * 0.35
    elif season == "Winter":
        body_type = "Jeep"
        total = budget * 0.65

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        body_type = "Cabrio"
        total = budget * 0.45
    elif season == "Winter":
        body_type = "Jeep"
        total = budget * 0.8

elif budget >= 500:
    car_class = "Luxury class"
    body_type = "Jeep"
    total = budget * 0.9

print(car_class)
print(f"{body_type} - {total:.2f}")
