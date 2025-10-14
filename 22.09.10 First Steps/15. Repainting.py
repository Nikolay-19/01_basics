nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
bags = 0.4

nylon = int(input())
paint = int(input())
thinner = int(input())
time = int(input())

nylon_total = (nylon + 2) * nylon_price
paint_total = (paint * 0.1 + paint) * paint_price
thinner_total = thinner * thinner_price
materials_total = paint_total + nylon_total + thinner_total + bags
workers_rate = (materials_total * 0.3) * time
price_total = materials_total + workers_rate

print(f"{price_total:.2f}")
