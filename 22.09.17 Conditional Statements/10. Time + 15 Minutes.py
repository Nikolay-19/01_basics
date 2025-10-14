hours = int(input())
minutes = int(input())
future = minutes + 15

if future >= 60:
    hours = hours + 1
    future = future - 60
if hours >= 24:
    hours = hours - 24
if future <= 9:
    print(f"{hours}:0{future}")
else:
    print(f"{hours}:{future}")
    