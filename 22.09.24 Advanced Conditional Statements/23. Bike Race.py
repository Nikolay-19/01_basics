junior = int(input())
senior = int(input())
track = str(input())

total = 0
left = 0

if track == "trail":
    junior_pr = 5.5
    senior_pr = 7
    total = junior_pr * junior +  senior_pr * senior
    expenses = total * 0.05
    left = total - expenses

elif track == "cross-country":
    if junior + senior < 50:
        junior_pr = 8
        senior_pr = 9.5
    elif junior + senior >= 50:
        junior_pr = 8 - 8 * 0.25
        senior_pr = 9.5 - 9.5 * 0.25
    total = junior_pr * junior + senior_pr * senior
    expenses = total * 0.05
    left = total - expenses

elif track == "downhill":
    junior_pr = 12.25
    senior_pr = 13.75
    total = junior_pr * junior + senior_pr * senior
    expenses = total * 0.05
    left = total - expenses

elif track == "road":
    junior_pr = 20
    senior_pr = 21.50
    total = junior_pr * junior + senior_pr * senior
    expenses = total * 0.05
    left = total - expenses

print(f"{left:.2f}")
