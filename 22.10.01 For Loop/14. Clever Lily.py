age = int(input())
washer_pr = float(input())
toy_pr = int(input())
toy_qt = 0
savings = 0
sub_total = 0
stolen = 0

for a in range(1, age + 1):
    if a % 2 == 0:
        savings += 10
        sub_total += savings
        stolen += 1
    else:
        toy_qt += 1
        
total = (sub_total + toy_qt * toy_pr) - washer_pr - stolen

if total >= 0:
    print(f"Yes! {total:.2f}")
else:
    print(f"No! {abs(total):.2f}")
    