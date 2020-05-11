number = str(input())

sum_kids = 0
sum_adults = 0
counter_kids = 0
counter_adults = 0

while number != 'Christmas':
    current_number = int(number)
    if current_number <= 16:
        sum_kids += current_number
        counter_kids += 1
        number = input()
    else:
        sum_adults += current_number
        counter_adults += 1
        number = input()

money_for_toys = counter_kids * 5
money_for_sweters = counter_adults * 15

print(f"Number of adults: {counter_adults}")
print(f"Number of kids: {counter_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweters}")