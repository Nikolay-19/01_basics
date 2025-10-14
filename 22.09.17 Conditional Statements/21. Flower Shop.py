import math
magnolia_qt = int(input())
zumbul_qt = int(input())
rose_qt = int(input())
cactus_qt = int(input())
gift_pr = float(input())

magnolia_pr = 3.25
zumbul_pr = 4
rose_pr = 3.5
cactus_pr = 8
sub_total = magnolia_pr * magnolia_qt + zumbul_pr * zumbul_qt + rose_pr * rose_qt + cactus_pr * cactus_qt
total = sub_total - (sub_total * 0.05)
left = abs(total - gift_pr)

if total >= gift_pr:
    print(f"She is left with {math.floor(left)} leva.")
if total < gift_pr:
    print(f"She will have to borrow {math.ceil(left)} leva.")
    