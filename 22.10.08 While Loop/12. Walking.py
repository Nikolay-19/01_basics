goal = 10000
total = 0
steps = input()

while steps != "Going home":
    steps = int(steps)
    total += steps
    if total >= goal:
        break
    steps = input()
    
if steps == "Going home":
    home = int(input())
    total = total + home
diff = abs(total - goal)

if total >= goal:
    print(f"Goal reached! Good job!\n"
          f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
    