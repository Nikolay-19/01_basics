budget = float(input())
gpu_qt = int(input())
cpu_qt = int(input())
ram_qt = int(input())

gpu_pr = 250
cpu_pr = gpu_pr * gpu_qt * 0.35
ram_pr = gpu_pr * gpu_qt * 0.1
sub_total = gpu_pr * gpu_qt + cpu_pr * cpu_qt + ram_pr * ram_qt

if gpu_qt >= cpu_qt:
    total = sub_total - sub_total * 0.15
else:
    total = sub_total

money_left = abs(budget - total)

if budget >= total:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")
    