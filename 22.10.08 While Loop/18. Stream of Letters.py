import string
text1 = ""
text2 = ""
command = ""

while True:
    command = input()
    if command == "End":
        break
    if command not in string.ascii_letters:
        continue
        
    if (command == "c" and "c" not in text2) or (command == "n" and "n" not in text2) or (command == "o" and "o" not in text2):
        text2 += command
    else:
        text1 += command
        
    if "c" in text2 and "n" in text2 and "o" in text2:
        text1 += " "
        print(text1, end="")
        text1 = ""
        text2 = ""
        