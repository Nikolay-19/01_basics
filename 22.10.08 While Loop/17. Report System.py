total = 0
count = 1
cash_qt = 0
card_qt = 0
cash_total = 0
card_total = 0
goal = int(input())

while total < goal:
    command = input()
    count += 1
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    command = int(command)
    
    if not (0 < command < 10 or (command > 100 and count % 2 == 0)):
        total += command
        if count % 2 == 0:
            cash_qt += 1
            cash_total += command
            print("Product sold!")
        else:
            card_qt += 1
            card_total += command
            print("Product sold!")
            
    elif command >= 100:
        if count % 2 == 0:
            print("Error in transaction!")
        else:
            card_qt += 1
            total += command
            card_qt += command
            print("Product sold!")
            
    elif 0 < command <= 10:
        if count % 2 == 0:
            cash_qt += 1
            cash_total += command
            total += command
            print("Product sold!")
        else:
            print("Error in transaction!")
            
else:
    cash_average = cash_total / cash_qt
    card_average = card_total / card_qt
    print(f"Average CS: {cash_average:.2f}\n"
          f"Average CC: {card_average:.2f}")
          