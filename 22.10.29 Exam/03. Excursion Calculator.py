people_qt = int(input())
season = input()
total = 0
if people_qt <= 5:
    if season == "spring":
        total = people_qt * 50
    elif season == "summer":
        total = people_qt * 48.5 * 0.85
    elif season == "autumn":
        total = people_qt * 60
    elif season == "winter":
        total = people_qt * 86 * 1.08
else:
    if season == "spring":
        total = people_qt * 48
    elif season == "summer":
        total = people_qt * 45. * 0.85
    elif season == "autumn":
        total = people_qt * 49.5
    elif season == "winter":
        total = people_qt * 85 * 1.08
print(f"{total:.2f} leva.")