command = str(input())

sum_kids = 0
sum_adults = 0
counter_kids = 0
counter_adults = 0
number = 0

while number != "Christmas":
    number = int(command)
    if number <= 16:
        current_number = int(number)
        sum_kids += current_number
        counter_kids += 1
    elif number > 16:
        current_number = int(number)
        sum_adults += current_number
        counter_adults += 1

print(f"Number of adults: {counter_adults}")
print(f"Number of kids: {counter_kids}")
print(f"Money for toys: {sum_kids}")
print(f"Money for sweaters: {sum_adults}")