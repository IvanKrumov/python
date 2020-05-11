import sys

n = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for i in range(1, n+1):
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number


sum_numbers -= max_number

if sum_numbers  == max_number:
    print("Yea")
else:
    print("No")


