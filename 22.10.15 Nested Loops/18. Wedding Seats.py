last_sector = ord(input()[0])
first_row = int(input())
odd_seats = int(input())
even_seats = odd_seats + 2
seats = 0
sector = 64
row = 0
seat = 96
count = 0

for a in range(65, last_sector + 1):
    sector += 1
    if a != 65:
        first_row += 1
        
    for b in range(1, first_row + 1):
        seat = 96
        row += 1
        
        if b == 1 or b % 2 != 0:
            seats = odd_seats
        else:
            seats = odd_seats + 2
            
        for c in range(1, seats + 1):
            seat += 1
            count += 1
            print(f"{chr(sector)}{b}{chr(seat)}")
            
print(count)
