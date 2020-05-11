import sys
count_numbers = int(input())

counter = 0
max_number = -sys.maxsize

while counter < count_numbers:
    current_number = int(input())
    if counter == 0:
        max_number = current_number

    if current_number > max_number:
        max_number = current_number

    counter += 1

print(max_number)