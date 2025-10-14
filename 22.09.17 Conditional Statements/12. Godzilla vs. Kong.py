budget = float(input())
extras = int(input())
costume_price = float(input())

sets = budget * 0.1
costumes = extras * costume_price

if extras >= 150:
    costumes = costumes - costumes * 0.1

expenses = sets + costumes
money_left = budget - expenses

if money_left >= 0:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
if money_left < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
    