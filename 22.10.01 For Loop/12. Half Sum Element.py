import sys
a = int(input())
total = 0
max_number = -sys.maxsize

for b in range(1, a + 1):
    c = int(input())
    total += c
    if c > max_number:
        max_number = c
        
if max_number == total - max_number:
    print(f"Yes")
    print(f"Sum = {total - max_number}")
else:
    print(f"No")
    print(f"Diff = {abs(total - max_number - max_number)}")
    