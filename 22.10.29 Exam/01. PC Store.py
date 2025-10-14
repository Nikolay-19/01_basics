usd_bgn = 1.57
cpu_usd_pr = float(input())
gpu_usd_pr = float(input())
ram_usd_pr = float(input())
ram_qt = int(input())
discount = float(input())
total = (cpu_usd_pr * 1.57 + gpu_usd_pr * 1.57 + ram_usd_pr * 1.57 * ram_qt) - (cpu_usd_pr * 1.57 * discount + gpu_usd_pr * 1.57 * discount)
print(f"Money needed - {total:.2f} leva.")