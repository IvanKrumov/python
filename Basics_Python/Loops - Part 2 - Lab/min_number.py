import sys
count_numbers = int(input())

counter = 0
min_number = sys.maxsize

while counter < count_numbers:
    number = int(input())
    if counter == 0:
        min_number = number
    if number < min_number:
        min_number = number

    counter += 1

print(min_number)