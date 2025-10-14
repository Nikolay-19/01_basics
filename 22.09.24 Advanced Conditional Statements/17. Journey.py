budget = float(input())
season = str(input())

destination = ""
accommodation = ""
total = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        total = budget - (budget * 0.7)
    elif season == "winter":
        accommodation = "Hotel"
        total = budget - (budget * 0.3)
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        total = budget - (budget * 0.6)
    elif season == "winter":
        accommodation = "Hotel"
        total = budget - (budget * 0.2)
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    total = budget - (budget * 0.1)

print(f"Somewhere in {destination}")
print(f"{accommodation} - {total:.2f}")
