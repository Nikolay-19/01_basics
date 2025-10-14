inheritance = float(input())
start_year = 1800
end_year = int(input())
age = 17
expenses = 0

for a in range(start_year, end_year + 1):
    if a % 2 == 0:
        age += 1
        expenses += 12000
    else:
        age += 1
        expenses += 12000 + 50 * age
        
total = inheritance - expenses

if total >= 0:
    print(f"Yes! He will live a carefree life and will have {total:.2f} dollars left.")
else:
    print(f"He will need {abs(total):.2f} dollars to survive.")
    