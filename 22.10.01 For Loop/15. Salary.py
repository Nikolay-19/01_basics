tabs = int(input())
salary = float(input())

for a in range(1, tabs + 1):
    b = str(input())
    if b == "Facebook":
        salary -= 150
    if b == "Instagram":
        salary -= 100
    if b == "Reddit":
        salary -= 50
        
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")
    