a = int(input())
b = int(input())
c = int(input())

for d in range(1, a + 1):
    for e in range(1, b + 1):
        for f in range(1, c + 1):
            if (d % 2 == 0 and f % 2 == 0) and (e == 2 or e == 3 or e == 5 or e == 7):
                print(d, e, f)
                