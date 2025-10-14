age = float(input())
pronoun = str(input())

if pronoun == "m":
    if age >= 16:
        print("Mr.")
    elif age < 16:
        print("Master")
elif pronoun == "f":
    if age >= 16:
        print("Ms.")
    elif age < 16:
        print("Miss")
        