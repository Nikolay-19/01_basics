a = int(input())
b = int(input())
command = str(input())
total = 0

if b == 0:
        print(f"Cannot divide {a} by zero")
elif command == "+":
    total = a + b
    if total % 2 == 0:
        print(f"{a} {command} {b} = {total} - even")
    else:
        print(f"{a} {command} {b} = {total} - odd")
elif command == "-":
    total = a - b
    if total % 2 == 0:
        print(f"{a} {command} {b} = {total} - even")
    else:
        print(f"{a} {command} {b} = {total} - odd")
elif command == "*":
    total = a * b
    if total % 2 == 0:
        print(f"{a} {command} {b} = {total} - even")
    else:
        print(f"{a} {command} {b} = {total} - odd")
elif command == "/":
    total = a / b
    print(f"{a} {command} {b} = {total:.2f}")
elif command == "%":
    total = a % b
    print(f"{a} {command} {b} = {total}")
    