start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter = 0
is_found = False

# first number -> from start_number to end_number

for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        counter += 1
        if first_number + second_number == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
            break
    if is_found:
        break
if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
