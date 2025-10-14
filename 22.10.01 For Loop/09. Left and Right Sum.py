a = int(input())
total1 = 0
total2 = 0

for b in range(1, a+1):
    c = int(input())
    total1 += c
    
for c in range(1, a+1):
    d = int(input())
    total2 += d
    
if total1 == total2:
    print(f"Yes, sum = {total1}")
if total1 != total2:
    print(f"No, diff = {abs(total1 - total2)}")
    