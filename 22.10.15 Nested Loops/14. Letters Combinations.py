start_letter = ord(input()[0])
end_letter = ord(input()[0])
break_letter = ord(input()[0])
count = 0

for a in range(start_letter, end_letter + 1):
    for b in range(start_letter, end_letter + 1):
        for c in range(start_letter, end_letter + 1):
            if a != break_letter and b != break_letter and c != break_letter:
                count += 1
                print(chr(a) + chr(b) + chr(c), end=" ")
                
print(count)
