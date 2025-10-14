water_pr = 20
internet_pr = 15
length = int(input())
water_total = 0
internet_total = 0
electricity_total = 0
misc_total = 0
total = 0

for _ in range(1, length + 1):
    electricity_pr = float(input())
    misc = (water_pr + internet_pr + electricity_pr) * 1.2
    total += water_pr + internet_pr + electricity_pr + misc
    water_total += water_pr
    internet_total += internet_pr
    electricity_total += electricity_pr
    misc_total += misc
    
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {misc_total:.2f} lv")
print(f"Average: {total / length:.2f} lv")
