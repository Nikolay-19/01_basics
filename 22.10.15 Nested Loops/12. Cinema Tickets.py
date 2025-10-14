flag = False
kid = 0
student = 0
standard = 0
kid_average = 0
sold_tickets = 0
total_tickets = 0
movie_average = 0
student_average = 0
standard_average = 0

while True:
    movie = input()
    if movie == "Finish":
        kid_average = kid / total_tickets * 100
        student_average = student / total_tickets * 100
        standard_average = standard / total_tickets * 100
        print(f"Total tickets: {total_tickets}\n"
              f"{student_average:.2f}% student tickets.\n"
              f"{standard_average:.2f}% standard tickets.\n"
              f"{kid_average:.2f}% kids tickets.")
        flag = True
        break
        
    if flag:
        break
    available_seats = int(input())
    available_seats2 = available_seats
    
    while available_seats > 0:
        ticket = input()
        if ticket == "End":
            total_tickets += sold_tickets
            movie_average = sold_tickets / available_seats2 * 100
            print(f"{movie} - {movie_average:.2f}% full.")
            sold_tickets = 0
            # flag = True
            break
            
        if ticket == "student":
            student += 1
            sold_tickets += 1
            available_seats -= 1
            
        if ticket == "standard":
            standard += 1
            sold_tickets += 1
            available_seats -= 1
            
        if ticket == "kid":
            kid += 1
            sold_tickets += 1
            available_seats -= 1
            
    else:
        total_tickets += sold_tickets
        movie_average = sold_tickets / available_seats2 * 100
        print(f"{movie} - {movie_average:.2f}% full.")
        sold_tickets = 0
        continue
        