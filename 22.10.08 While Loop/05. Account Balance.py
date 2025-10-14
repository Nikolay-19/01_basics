operation = ""
total = 0

while operation != "NoMoreMoney":
    operation = input()
    if operation == "NoMoreMoney":
        break
    operation = float(operation)
    if operation > 0:
        total += operation
        print(f"Increase: {operation:.2f}")
    else:
        print("Invalid operation!")
        break
        
print(f"Total: {total:.2f}")
