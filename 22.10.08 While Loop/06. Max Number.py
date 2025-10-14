import sys
a = ""
max_number = -sys.maxsize
min_number = sys.maxsize

while a != "Stop":
    a = input()
    if a == "Stop":
        break
    a = int(a)
    if a > max_number:
        max_number = a
    if a < min_number:
        min_number = a
        
print(max_number)
