a = int(input())
b = int(input())
c = int(input())
total = 0
total2 = 0
flag = False

for d in range(a, b + 1):
    for e in range(a, b + 1):
        total += 1
        
        if d + e == c:
            total2 += 1
            print(f"Combination N:{total} ({d} + {e} = {c})")
            flag = True
            break
            
    if flag:
        break
        
if total2 == 0:
    print(f"{total} combinations - neither equals {c}")
    