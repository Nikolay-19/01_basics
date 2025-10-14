total = 0
total2 = 0
average = 0
average2 = 0
grade_qt = 0
flag = False
jury = int(input())

while True:
    lesson = str(input())
    if lesson == "Finish":
        print(f"Student's final assessment is {average2:.2f}.")
        flag = True
        break
    if flag:
        break
        
    for a in range(1, jury + 1):
        grade = float(input())
        grade_qt += 1
        total += grade
        total2 += grade
        
    average = total / jury
    average2 = total2 / grade_qt
    print(f"{lesson} - {average:.2f}.")
    total = 0
    average = 0
    