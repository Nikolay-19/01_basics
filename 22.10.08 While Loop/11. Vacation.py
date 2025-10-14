vacation_pr = float(input())
available = float(input())
days = 0
days_total = 0
total = 0

while True:
    action = str(input())
    amount = float(input())
    days_total += 1
    
    if action == "save":
        total += amount
        days = 0
        
    if action == "spend":
        days += 1
        available -= amount
        if available <= 0:
            total = 0
            available = 0
            
    if days == 5:
        print(f"You can't save the money.\n"
              f"{days_total}")
        break
        
    if total + available >= vacation_pr:
        print(f"You saved the money for {days_total} days.")
        break
        