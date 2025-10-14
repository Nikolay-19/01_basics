length = int(input())
accommodation = str(input())
feedback = str(input())

room_pr = 18
apartment_pr = 25
president_pr = 35
total = 0

if accommodation == "room for one person":
    total = (length-1) * room_pr

if accommodation == "apartment":
    if length < 10:
        apartment_pr = apartment_pr * 0.7
    if 10 <= length <= 15:
        apartment_pr = apartment_pr * 0.65
    if length > 15:
        apartment_pr = apartment_pr * 0.5
    total = apartment_pr * (length-1)

if accommodation == "president apartment":
    if length < 10:
        president_pr = president_pr * 0.9
    if 10 <= length <= 15:
        president_pr = president_pr * 0.85
    if length > 15:
        president_pr = president_pr * 0.8
    total = president_pr * (length-1)

if feedback == "positive":
    total = total + total * 0.25
if feedback == "negative":
    total = total - total * 0.1

print(f"{total:.2f}")
