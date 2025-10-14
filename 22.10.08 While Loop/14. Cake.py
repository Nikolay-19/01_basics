width = int(input())
length = int(input())
taken = 0
total = width * length
left = total

while left > 0:
    command = input()
    if command == "STOP":
        print(f"{abs(left)} pieces are left.")
        break
    command = int(command)
    taken -= command
    left = total + taken
else:
    print(f"No more cake left! You need {abs(left)} pieces more.")
    