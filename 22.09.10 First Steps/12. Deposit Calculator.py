deposit = float(input())
time = int(input())
rate = float(input()) /100
total = deposit + time * ((deposit * rate)/12)
print(f"{total:.2f}")