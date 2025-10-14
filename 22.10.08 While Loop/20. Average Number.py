a = int(input())
total = 0

for b in range(1, a + 1):
    c = int(input())
    total += c
    average = total / a
    
print(f"{average:.2f}")
