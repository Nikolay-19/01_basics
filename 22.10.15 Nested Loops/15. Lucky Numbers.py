a = int(input())

for b in range(1, 10):
    for c in range(1, 10):
        for d in range(1, 10):
            for e in range(1, 10):
                if (b + c) == (d + e) and (a % (b + c) == 0):
                    print(f"{b}{c}{d}{e}", end=" ")
                    