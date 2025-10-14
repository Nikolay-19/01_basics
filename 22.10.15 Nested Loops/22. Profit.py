one_lev = int(input())
two_leva = int(input())
five_leva = int(input())
total = int(input())

for a in range(0, one_lev + 1):
    for b in range(0, two_leva + 1):
        for c in range(0, five_leva + 1):
            if a * 1 + b * 2 + c * 5 == total and not a > one_lev and not b > two_leva and not c > five_leva:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total} lv.")
                