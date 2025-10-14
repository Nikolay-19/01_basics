men_qt = int(input())
women_qt = int(input())
tables = int(input())
flag = False

for a in range(1, men_qt + 1):
    for b in range(1, women_qt + 1):
        tables -= 1
        print(f"({a} <-> {b})", end=" ")
        if tables <= 0:
            flag = True
            break
            
    if flag:
        break
        