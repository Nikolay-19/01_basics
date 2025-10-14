a = int(input())
total = 0
flag = False

for b in range(1, a + 1):
    for c in range(1, b + 1):
        total += 1
        
        if total > a:
            flag = True
            break
        print(total, end=" ")
        
    if flag:
        break
    print()
    