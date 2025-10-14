time = int(input())
doctors = 7
treated = 0
untreated = 0

for a in range(1, time + 1):
    if a % 3 == 0:
        if untreated > treated:
            doctors += 1
    patients_today = int(input())
    
    if doctors < patients_today:
        diff = patients_today - doctors
        untreated += diff
        treated += doctors
    else:
        treated += patients_today
        
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
