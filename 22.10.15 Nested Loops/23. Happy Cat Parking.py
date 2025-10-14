days = int(input())
hours = int(input())
day_total = 0
total = 0

for a in range(1, days + 1):
    for b in range(1, hours + 1):
        if a % 2 == 0 and b % 2 != 0:
            day_total += 2.5
        elif a % 2 != 0 and b % 2 == 0:
            day_total += 1.25
        else:
            day_total += 1
            
    print(f"Day: {a} - {day_total:.2f} leva")
    total += day_total
    day_total = 0
    
print(f"Total: {total:.2f} leva")
