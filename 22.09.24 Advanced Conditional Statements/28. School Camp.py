season = str(input())
gender = str(input())
head_count = int(input())
length = int(input())

sport = ""
price_single = 0
price_mixed = 0
total = 0

if season == "Winter":
    price_single = 9.6
    price_mixed = 10
    if gender == "boys":
        sport = "Judo"
    if gender == "girls":
        sport = "Gymnastics"
    if gender == "mixed":
        sport = "Ski"
    if gender == "boys" or gender == "girls":
        if head_count < 10:
            total = head_count * price_single * length
        elif 10 <= head_count < 20:
            total = (head_count * price_single * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_single * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_single * length) * 0.5
    elif gender == "mixed":
        if head_count < 10:
            total = head_count * price_mixed * length
        elif 10 <= head_count < 20:
            total = (head_count * price_mixed * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_mixed * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_mixed * length) * 0.5

elif season == "Spring":
    price_single = 7.2
    price_mixed = 9.5
    if gender == "boys":
        sport = "Tennis"
    if gender == "girls":
        sport = "Athletics"
    if gender == "mixed":
        sport = "Cycling"
    if gender == "boys" or gender == "girls":
        if head_count < 10:
            total = head_count * price_single * length
        elif 10 <= head_count < 20:
            total = (head_count * price_single * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_single * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_single * length) * 0.5
    elif gender == "mixed":
        if head_count < 10:
            total = head_count * price_mixed * length
        elif 10 <= head_count < 20:
            total = (head_count * price_mixed * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_mixed * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_mixed * length) * 0.5

if season == "Summer":
    price_single = 15
    price_mixed = 20
    if gender == "boys":
        sport = "Football"
    if gender == "girls":
        sport = "Volleyball"
    if gender == "mixed":
        sport = "Swimming"
    if gender == "boys" or gender == "girls":
        if head_count < 10:
            total = head_count * price_single * length
        elif 10 <= head_count < 20:
            total = (head_count * price_single * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_single * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_single * length) * 0.5
    elif gender == "mixed":
        if head_count < 10:
            total = head_count * price_mixed * length
        elif 10 <= head_count < 20:
            total = (head_count * price_mixed * length) * 0.95
        elif 20 <= head_count < 50:
            total = (head_count * price_mixed * length) * 0.85
        elif head_count >= 50:
            total = (head_count * price_mixed * length) * 0.5

print(f"{sport} {total:.2f} lv.")
