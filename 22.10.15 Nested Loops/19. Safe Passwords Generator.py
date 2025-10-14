a = int(input())
b = int(input())
c = int(input())
count = 0
flag = False

for d in range(34, 55):
    for e in range(63, 96):
        for h in range(63, 96):
            for j in range(34, 55):
                for f in range(1, a + 1):
                    for g in range(1, b + 1):
                        if d >= 55:
                            d = 34
                        if e >= 96:
                            e = 63
                        if j >= 55:
                            j = 34
                        if h >= 96:
                            h = 63
                        count += 1
                        d += 1
                        e += 1
                        h += 1
                        j += 1
                        print(f"{chr(d)}{chr(e)}{f}{g}{chr(h)}{chr(j)}", end="|")
                        
                        if count >= c:
                            flag = True
                            break
                        if a == f and b == g:
                            flag = True
                            break
                    
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
        