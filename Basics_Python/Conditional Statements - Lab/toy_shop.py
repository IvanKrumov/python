trip = float(input())
puzzels_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
cars_count = int(input())


Count_total = puzzels_count + dolls_count + bears_count + minions_count + cars_count
Sum_total = (puzzels_count * 2.60) + (dolls_count * 3) + (bears_count * 4.10) + (minions_count * 8.20) + (cars_count * 2)

if Count_total >= 50:
    Sum = Sum_total * 0.75
    Sum1 = Sum * 0.9
    if Sum1 >= trip:
        sum_left = abs(Sum1 - trip)
        print(f'Yes! {sum_left:.2f} lv left.')
    else:
        sum_need = abs(Sum1 - trip)
        print(f'Not enough money! {sum_need:.2f} lv needed.')
else:
    Sum = Sum_total * 0.9
    if Sum >= trip:
        sum_left = abs(Sum - trip)
        print(f'Yes! {sum_left:.2f} lv left.')
    else:
        sum_need = abs(Sum - trip)
        print(f'Not enough money! {sum_need:.2f} lv needed.')



