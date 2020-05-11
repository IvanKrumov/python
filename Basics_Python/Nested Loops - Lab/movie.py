name = input()
count_total_tickets = 0
count_student_tickets = 0
count_standard_ticket = 0
count_kid_ticket = 0

while name != "Finish":
    seats = int(input())
    count_tickets = 0
    movie_type = input()
    while movie_type != "End":
        if movie_type == "student":
            count_student_tickets += 1
        elif movie_type == "standard":
            count_standard_ticket += 1
        elif movie_type == "kid":
            count_kid_ticket += 1
        count_tickets += 1
        count_total_tickets += 1
        if count_tickets >= seats:
            break
        movie_type = input()

    percent = count_tickets / seats * 100
    print(f"{name} - {percent:.2f}% full.")
    name = input()

if name == "Finish":
    print(f"Total tickets: {count_total_tickets}")

    percent_student = count_student_tickets / count_total_tickets * 100
    print(f"{percent_student:.2f}% student tickets.")

    percent_standard = count_standard_ticket / count_total_tickets * 100
    print(f"{percent_standard:.2f}% standard tickets.")

    percent_kid = count_kid_ticket / count_total_tickets * 100
    print(f"{percent_kid:.2f}% kids tickets.")
