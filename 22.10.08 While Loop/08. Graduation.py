name = str(input())
year = 0
fail = 0
total = 0

while True:
    if fail >= 2:
        print(f"{name} has been excluded at {year+1} grade")
        break
    if year == 12:
        average = total / year
        print(f"{name} graduated. Average grade: {average:.2f}")
        break
        
    grade = float(input())
    
    if 4 <= grade <= 6:
        year += 1
        total += grade
    elif 2 <= grade < 4:
        year == year
        fail += 1
        