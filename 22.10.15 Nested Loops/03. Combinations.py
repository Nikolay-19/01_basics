a = int(input())
total = 0

for b in range(0, a + 1):
    for c in range(0, a+1):
        for d in range(0, a+1):
            if b + c + d == a:
                total += 1
                
print(total)
