width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
left = volume

while left > 0:
    command = input()
    if command == "Done":
        print(f"{left} Cubic meters left.")
        break
    command = int(command)
    left -= command
else:
    print(f"No more free space! You need {abs(left)} Cubic meters more.")
    