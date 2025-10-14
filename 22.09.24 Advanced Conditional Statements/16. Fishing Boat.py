budget = int(input())
season = str(input())
fishermen = int(input())

spring_pr = 3000
summer_autumn_pr = 4200
winter_pr = 2600
total = 0
left = 0

if season == "Spring":
    if fishermen <= 6:
        total = spring_pr - (spring_pr * 0.1)
        left = budget - total
    elif 7 <= fishermen <= 11:
        total = spring_pr - (spring_pr * 0.15)
        left = budget - total
    elif fishermen >= 12:
        total = spring_pr - (spring_pr * 0.25)
        left = budget - total
elif season == "Summer" or season == "Autumn":
    if fishermen <= 6:
        total = summer_autumn_pr - (summer_autumn_pr * 0.1)
        left = budget - total
    elif 7 <= fishermen <= 11:
        total = summer_autumn_pr - (summer_autumn_pr * 0.15)
        left = budget - total
    elif fishermen >= 12:
        total = summer_autumn_pr - (summer_autumn_pr * 0.25)
        left = budget - total
elif season == "Winter":
    if fishermen <= 6:
        total = winter_pr - (winter_pr * 0.1)
        left = budget - total
    elif 7 <= fishermen <= 11:
        total = winter_pr - (winter_pr * 0.15)
        left = budget - total
    elif fishermen >= 12:
        total = winter_pr - (winter_pr * 0.25)
        left = budget - total

if fishermen % 2 == 0 and season != "Autumn":
    total = total - (total * 0.05)
    left = budget - total


if left >= 0:
    print(f"Yes! You have {left:.2f} leva left.")
if left < 0:
    print(f"Not enough money! You need {abs(left):.2f} leva.")
    