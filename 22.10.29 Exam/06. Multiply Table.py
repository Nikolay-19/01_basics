number = int(input())
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
for a in range(1, units + 1):
    for b in range(1, tens + 1):
        for c in range(1, hundreds + 1):
            print(f"{a} * {b} * {c} = {a*b*c};")