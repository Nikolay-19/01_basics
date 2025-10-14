import string
a = int(input())
b = int(input())

for c in range(1, a + 1):
    for d in range(1, a + 1):
        for e in range(97, 97 + b):
            for f in range(97, 97 + b):
                for g in range(1, a + 1):
                    if g > c and g > d:
                        print(f"{c}{d}{chr(e)}{chr(f)}{g}", end=" ")
                        