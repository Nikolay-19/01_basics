total = 0
while True:
    destination = input()
    if destination == "End":
        break
        
    goal = float(input())
    savings = float(input())
    total += savings
    
    while total < goal:
        savings = float(input())
        total += savings
        
    if total >= goal:
        total = 0
        print(f"Going to {destination}!")
        continue
        