a = int(input())
totalE = 0
totalO = 0

for b in range(1, a + 1):
    c = int(input())
    if b % 2 == 0:
        totalE += c
    else:
        totalO += c
        
if totalO == totalE:
    print("Yes")
    print(f"Sum = {totalE}")
else:
    print("No")
    print(f"Diff = {abs(totalE - totalO)}")
    