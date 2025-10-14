import sys
max_number = -sys.maxsize
min_number = sys.maxsize
a = int(input())

for i in range(1, a + 1):
    b = int(input())
    if b > max_number:
        max_number = b
    if b < min_number:
        min_number = b
        
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
