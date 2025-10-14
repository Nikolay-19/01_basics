chicken_price = 10.35
fish_price = 12.40
veg_price = 8.15
delivery_price = 2.5

chicken = int(input())
fish = int(input())
veg = int(input())

sub_total = chicken * chicken_price + fish * fish_price + veg * veg_price
desert = sub_total * 0.2
total = sub_total + desert + delivery_price

print(f"{total:.2f}")
