first_num = int(input())
second_num = int(input())
third_num = int(input())
flag = False
prime = 0
p = 0
i = 0
n = 0
for p1 in range(1, first_num + 1):
    if p1 % 2 == 0:
        p = p1
    else:
        continue
    for i1 in range(2, second_num + 1):
        if (i1 == 4 or i1 == 6 or i1 == 8 or i1 == 9 or i1 == 10) and (i1 <= second_num + 1):
            continue
        else:
            i = i1
        for n1 in range(1, third_num + 1):
            if n1 % 2 == 0:
                n = n1
                print(p, i, n)
        else:
            continue
            