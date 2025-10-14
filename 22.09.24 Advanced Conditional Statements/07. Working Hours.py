time = int(input())
day = str(input())

if 10 <= time <= 18 and day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    print("open")
else:
    print("closed")
    