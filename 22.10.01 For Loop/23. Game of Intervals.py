length = int(input())
score = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0

for a in range(1, length + 1):
    b = int(input())
    if 0 <= b <= 9:
        b1 += 1
        score += 0.2 * b
    if 10 <= b <= 19:
        b2 += 1
        score += 0.3 * b
    if 20 <= b <= 29:
        b3 += 1
        score += 0.4 * b
    if 30 <= b <= 39:
        b4 += 1
        score += 50
    if 40 <= b <= 50:
        b5 += 1
        score += 100
    if b < 0 or b > 50:
        b6 += 1
        score /= 2
        
total = b1 + b2 + b3 + b4 + b5 + b6
print(f"{score:.2f}")
print(f"From 0 to 9: {b1 / total * 100:.2f}%")
print(f"From 10 to 19: {b2 / total * 100:.2f}%")
print(f"From 20 to 29: {b3 / total * 100:.2f}%")
print(f"From 30 to 39: {b4 / total * 100:.2f}%")
print(f"From 40 to 50: {b5 / total * 100:.2f}%")
print(f"Invalid numbers: {b6 / total * 100:.2f}%")
