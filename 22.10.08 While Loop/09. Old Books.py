title1 = input()
total = 0

while True:
    title2 = input()
    total += 1
    if title2 == "No More Books":
        print(f"The book you search is not here!\n"
              f"You checked {total-1} books.")
        break
    if title1 == title2:
        print(f"You checked {total-1} books and found it.")
        break
        