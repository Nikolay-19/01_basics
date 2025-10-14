fail_margin = int(input())
fail = 0
grade = 0
average = 0
problems = 0
grade_sum = 0
problem_name = ""

while True:
    if 2 <= grade <= 4:
        fail += 1
        if fail == fail_margin:
            print(f"You need a break, {fail_margin} poor grades.")
            break
    problem_old = problem_name
    problem_name = str(input())
    
    if problem_name == "Enough":
        print(f"Average score: {average:.2f}\n"
              f"Number of problems: {problems}\n"
              f"Last problem: {problem_old}")
        break
        
    grade = int(input())
    problems += 1
    grade_sum += grade
    average = grade_sum / problems
    