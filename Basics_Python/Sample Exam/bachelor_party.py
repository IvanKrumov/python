singer = int(input())
places = 0
command = " "
total_money = 0
group_count_total = 0

while command != "The restaurant is full":
    command = input()
    if command == "The restaurant is full":
        break
    else:

        group_count = int(command)
        group_count_total += group_count
        if group_count < 5:
            profit = group_count * 100
        elif group_count >= 5:
            profit = group_count * 50

        total_money += profit

print(f"toral money {total_money}")

if total_money > singer:
    money_left = total_money - singer
    print(f"You have {group_count_total} guests and {money_left} leva left.")
else:
    print(f"You have {group_count_total} guests and {total_money} leva income, but no singer.")