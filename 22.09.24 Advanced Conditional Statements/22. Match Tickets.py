budget = float(input())
category = str(input())
fans = int(input())

vip_pr = 499.99
normal_pr = 249.99
total = 0
left = 0
transport = 0

if category == "VIP":
    if 1 <= fans <= 4:
        transport = budget * 0.75
    elif 5 <= fans <= 9:
        transport = budget * 0.6
    elif 10 <= fans <= 24:
        transport = budget * 0.5
    elif 25 <= fans <= 49:
        transport = budget * 0.4
    elif fans >= 50:
        transport = budget * 0.25
    total = fans * vip_pr
    left = budget - (transport + total)

if category == "Normal":
    if 1 <= fans <= 4:
        transport = budget * 0.75
    elif 5 <= fans <= 9:
        transport = budget * 0.6
    elif 10 <= fans <= 24:
        transport = budget * 0.5
    elif 25 <= fans <= 49:
        transport = budget * 0.4
    elif fans >= 50:
        transport = budget * 0.25
    total = fans * normal_pr
    left = budget - (transport + total)

if left >= 0:
    print(f"Yes! You have {left:.2f} leva left.")
elif left < 0:
    print(f"Not enough money! You need {abs(left):.2f} leva.")
    