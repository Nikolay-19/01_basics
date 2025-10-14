budget = float(input())
season = str(input())

accommodation = ""
location = ""
total = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        total = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        total = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        total = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        total = budget * 0.6
        
elif budget >= 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        total = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        total = budget * 0.9

print(f"{location} - {accommodation} - {total:.2f}")
