floors = int(input())
apts = int(input())
floor = ""
apt = ""

for a in range(floors, 0, - 1):
    for b in range(0, apts):
        if a == floors:
            floor = (f"L{a}")
            apt = b
        elif a % 2 == 0:
            floor = (f"O{a}")
            apt = b
        else:
            floor = (f"A{a}")
            apt = b
        print(f"{floor}{apt}", end=" ")
    print()
    