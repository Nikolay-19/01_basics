soap = 750
dish = 5
casserole = 15
count = 0
soap_qt = int(input()) * soap
dish_qt = 0
casserole_qt = 0

while soap_qt >= 0:
    command = input()
    count += 1
    
    if command == "End":
        print(f"Detergent was enough!\n"
              f"{dish_qt} dishes and {casserole_qt} pots were washed.\n"
              f"Leftover detergent {soap_qt} ml.")
        break
    command = int(command)
    
    if count % 3 == 0:
        casserole_qt += command
        soap_qt -= command * casserole
    else:
        dish_qt += command
        soap_qt -= command * dish
        
else:
    print(f"Not enough detergent, {abs(soap_qt)} ml. more necessary!")
    