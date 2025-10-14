check = int(input())
count = 0
passw = ""
flag = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if ((a * b + c * d) == check) and (a < b and c > d):
                    count += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if count == 4:
                        flag = True
                        passw = f"{a}{b}{c}{d}"

if flag:
    print(f"\nPassword: {passw}")
else:
    print("\nNo!")
    