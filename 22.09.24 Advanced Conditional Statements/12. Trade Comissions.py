city = str(input())
sales = float(input())
commission = 0

small_comm_S = 0.05
small_comm_V = 0.045
small_comm_P = 0.055
medium_comm_S = 0.07
medium_comm_V = 0.075
medium_comm_P = 0.08
big_comm_S = 0.08
big_comm_V = 0.1
big_comm_P = 0.12
very_big_comm_S = 0.12
very_big_comm_V = 0.13
very_big_comm_P = 0.145

if sales < 0 or city not in ["Sofia", "Varna", "Plovdiv"]:
    print("error")

elif city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * small_comm_S
    elif 500 < sales <= 1000:
        commission = sales * medium_comm_S
    elif 1000 < sales <= 10000:
        commission = sales * big_comm_S
    elif sales > 10000:
        commission = sales * very_big_comm_S
    print(f"{commission:.2f}")

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * small_comm_V
    elif 500 < sales <= 1000:
        commission = sales * medium_comm_V
    elif 1000< sales <= 10000:
        commission = sales * big_comm_V
    elif sales > 10000:
        commission = sales * very_big_comm_V
    print(f"{commission:.2f}")

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * small_comm_P
    elif 500 < sales <= 1000:
        commission = sales * medium_comm_P
    elif 1000< sales <= 10000:
        commission = sales * big_comm_P
    elif sales > 10000:
        commission = sales * very_big_comm_P
    print(f"{commission:.2f}")
    