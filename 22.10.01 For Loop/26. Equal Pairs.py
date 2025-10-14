import sys
a = int(input())
total = 0
max_number = -sys.maxsize
min_number = sys.maxsize

for b in range(1, a + 1):
    c = int(input())
    d = int(input())
    diff = abs(total - (c + d))
    total = c + d
    if total > max_number:
        max_number = total
    if total < min_number:
        min_number = total
        
if max_number == min_number:
    print(f"Yes, value={max_number}")
else:
    print(f"No, maxdiff={diff}")
    