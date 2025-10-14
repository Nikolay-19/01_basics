goal = int(input())
total = 0
while True:
    command = input()
    if command == "closed":
        break
    if command == "haircut":
        command = input()
        if command == "mens":
            total += 15
        if command == "ladies":
            total += 20
        if command == "kids":
            total += 10
    if command == "color":
        command = input()
        if command == "touch up":
            total += 20
        if command == "full color":
            total += 30
    if goal <= total:
        break
diff = abs(goal - total)
if goal <= total:
    print(f"You have reached your target for the day!\n"
          f"Earned money: {total}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.\n"
          f"Earned money: {total}lv.")