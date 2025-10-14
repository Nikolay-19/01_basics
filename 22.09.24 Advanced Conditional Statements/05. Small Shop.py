product = str(input())
city = str(input())
quantity = float(input())

coffee_S = 0.5
coffee_P = 0.4
coffee_V = 0.45
water_S = 0.8
water_P = 0.7
water_V = 0.7
beer_S = 1.2
beer_P = 1.15
beer_V = 1.1
sweets_S = 1.45
sweets_P = 1.3
sweets_V = 1.35
peanuts_S = 1.6
peanuts_P = 1.5
peanuts_V = 1.55

if city == "Sofia":
    if product == "coffee":
        total = quantity * coffee_S
        print(total)
    elif product == "water":
        total = quantity * water_S
        print(total)
    elif product == "beer":
        total = quantity * beer_S
        print(total)
    elif product == "sweets":
        total = quantity * sweets_S
        print(total)
    elif product == "peanuts":
        total = quantity * peanuts_S
        print(total)

elif city == "Plovdiv":
    if product == "coffee":
        total = quantity * coffee_P
        print(total)
    elif product == "water":
        total = quantity * water_P
        print(total)
    elif product == "beer":
        total = quantity * beer_P
        print(total)
    elif product == "sweets":
        total = quantity * sweets_P
        print(total)
    elif product == "peanuts":
        total = quantity * peanuts_P
        print(total)

if city == "Varna":
    if product == "coffee":
        total = quantity * coffee_V
        print(total)
    elif product == "water":
        total = quantity * water_V
        print(total)
    elif product == "beer":
        total = quantity * beer_V
        print(total)
    elif product == "sweets":
        total = quantity * sweets_V
        print(total)
    elif product == "peanuts":
        total = quantity * peanuts_V
        print(total)
        