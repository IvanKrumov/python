student_name = input()

grades_passed = 1
sum_marks = 0
exclude_counter = 0
is_expelled = False
while grades_passed <= 12:
    current_mark = float(input())
    if current_mark >= 4:
        grades_passed += 1
        sum_marks += current_mark
    else:
        exclude_counter += 1
        if exclude_counter > 1:
            is_expelled = True
            print(f"{student_name} has been excluded at {grades_passed} grade")
            break

if not is_expelled:
    average_mark = sum_marks / 12
    print(f"{student_name} graduated. Average grade: {average_mark:.2f}")


