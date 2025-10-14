a = int(input())
b = ""

for c in range(1111, 10000):
    thousands = (c // 1000) % 10
    hundreds = (c // 100) % 10
    tens = (c // 10) % 10
    units = c % 10
    
    if thousands != 0 and hundreds != 0 and tens != 0 and units != 0:
        if a % thousands == 0 and a % hundreds == 0 and a % tens == 0 and a % units == 0:
            print(f"{thousands}{hundreds}{tens}{units}", end=' ')
            