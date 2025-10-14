a = 0
prime = 0
nonprime = 0

while True:
    command = input()
    if command == "stop":
        break
    command = int(command)
    
    for b in range(1, command + 1):
        if command % b == 0:
            a += 1
            
    if command == 0 or command == 1:
        continue
    elif command < 0:
        print(f"Number is negative.")
        continue
        
    elif a == 2:
        prime += command
    else:
        nonprime += command
    a = 0
    
print(f"Sum of all prime numbers is: {prime}\n"
      f"Sum of all non prime numbers is: {nonprime}")
      