start = int(input())
end = int(input())
goal = int(input())
count = 0
flag = False

for a in range(start, end + 1):
    for b in range(start, end + 1):
        count += 1
        if a + b == goal:
            print(f"Combination N:{count} ({a} + {b} = {goal})")
            flag = True
            break
            
    if flag:
        break
        
else:
    print(f"{count} combinations - neither equals {goal}")
    