a = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for b in range(0, a):
    c = int(input())
    if c < 200:
        p1 += 1
    if 200 <= c < 400:
        p2 += 1
    if 400 <= c < 600:
        p3 += 1
    if 600 <= c < 800:
        p4 += 1
    if c >= 800:
        p5 += 1

total = p1 + p2 + p3 + p4 + p5
p1pr = p1 / total * 100
p2pr = p2 / total * 100
p3pr = p3 / total * 100
p4pr = p4 / total * 100
p5pr = p5 / total * 100

print(f"{p1pr:.2f}%")
print(f"{p2pr:.2f}%")
print(f"{p3pr:.2f}%")
print(f"{p4pr:.2f}%")
print(f"{p5pr:.2f}%")
