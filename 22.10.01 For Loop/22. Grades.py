students = int(input())
students5 = 0
students4 = 0
students3 = 0
students2 = 0
average = 0

for a in range(1, students + 1):
    grade = float(input())
    
    if grade < 3:
        students2 += 1
        average += grade
    if 3 <= grade < 4:
        students3 += 1
        average += grade
    if 4 <= grade < 5:
        students4 += 1
        average += grade
    if grade >= 5:
        students5 += 1
        average += grade
        
print(f"Top students: {students5 / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {students4 / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {students3 / students * 100:.2f}%")
print(f"Fail: {students2 / students * 100:.2f}%")
print(f"Average: {average / students:.2f}")
