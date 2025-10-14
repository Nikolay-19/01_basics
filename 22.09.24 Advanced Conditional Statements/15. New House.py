flowers = str(input())
quantity = int(input())
budget = int(input())

rose_pr = 5
dahlia_pr = 3.8
tulip_pr = 2.8
narcissus_pr = 3
gladiolus_pr = 2.5
total = 0
left = 0

if flowers == "Roses":
    if quantity > 80:
        total = quantity * rose_pr - (quantity * rose_pr * 0.1)
        left = budget - total
    elif quantity <= 80:
        total = quantity * rose_pr
        left = budget - total
if flowers == "Dahlias":
    if quantity > 90:
        total = quantity * dahlia_pr - (quantity * dahlia_pr * 0.15)
        left = budget - total
    elif quantity <= 90:
        total = quantity * dahlia_pr
        left = budget - total
if flowers == "Tulips":
    if quantity > 80:
        total = quantity * tulip_pr - (quantity * tulip_pr * 0.15)
        left = budget - total
    elif quantity <= 80:
        total = quantity * tulip_pr
        left = budget - total
if flowers == "Narcissus":
    if quantity < 120:
        total = quantity * narcissus_pr + (quantity * narcissus_pr * 0.15)
        left = budget - total
    elif quantity >= 120:
        total = quantity * narcissus_pr
        left = budget - total
if flowers == "Gladiolus":
    if quantity < 80:
        total = quantity * gladiolus_pr + (quantity * gladiolus_pr * 0.2)
        left = budget - total
    elif quantity >= 80:
        total = quantity * gladiolus_pr
        left = budget - total

if left >= 0:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {left:.2f} leva left.")
elif left < 0:
    print(f"Not enough money, you need {abs(left):.2f} leva more.")
    