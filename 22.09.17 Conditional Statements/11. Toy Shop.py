puzzle_price = 2.6
doll_price = 3
teddy_price = 4.1
minyon_price = 8.2
truck_price = 2

vacation_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
teddy_quantity = int(input())
minyon_quantity = int(input())
truck_quantity = int(input())

sub_total_price = puzzle_price * puzzle_quantity + doll_price * doll_quantity + teddy_price * teddy_quantity + minyon_price * minyon_quantity + truck_price * truck_quantity
total_quantity = puzzle_quantity + doll_quantity + teddy_quantity +minyon_quantity + truck_quantity

if total_quantity >= 50:
    total_income = sub_total_price - (sub_total_price * 0.25)
else:
    total_income = sub_total_price

rent = total_income * 0.1
profit = total_income - rent
money_left = abs(profit - vacation_price)

if vacation_price > profit:
    print(f"Not enough money! {money_left:.2f} lv needed.")
else:
    print(f"Yes! {money_left:.2f} lv left.")
    