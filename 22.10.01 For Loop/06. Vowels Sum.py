a = str(input())
total = 0
for b in range(0, len(a)):
    if a[b] == "a":
        total += 1
    if a[b] == "e":
        total += 2
    if a[b] == "i":
        total += 3
    if a[b] == "o":
        total += 4
    if a[b] == "u":
        total += 5
print(total)
