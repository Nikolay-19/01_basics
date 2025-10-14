season = str(input())
mileage = float(input())

salary = 0
total = 0
left = 0
tax = 0.1

if mileage <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = 0.75
    elif season == "Summer":
        salary = 0.9
    elif season == "Winter":
        salary = 1.05
    total = salary * mileage * 4
    left = total - (total * tax)

elif 5000 < mileage <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = 0.95
    elif season == "Summer":
        salary = 1.1
    elif season == "Winter":
        salary = 1.25
    total = salary * mileage * 4
    left = total - (total * tax)

elif 10000 < mileage <= 20000:
    salary = 1.45
    total = salary * mileage * 4
    left = total - (total * tax)

print(f"{left:.2f}")
