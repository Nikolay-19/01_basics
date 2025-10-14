for _ in range(1, 1000):
    a = float(input())
    if a >= 0:
        print(f"Result: {a * 2:.2f}")
    else:
        print("Negative number!")
        break
        