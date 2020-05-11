needed_money = float(input())
owned_money = float(input())

money_spend = 0
money_saved = 0
days_spend = 0
days_total = 0


while owned_money < needed_money:
    action = input()
    if action == 'save':
        money_saved = float(input())
        owned_money += money_saved
    if action == 'spend':
        money_spend = float(input())
        if money_spend >= owned_money:
            owned_money = 0
        else:
            owned_money -= money_spend
            days_spend += 1
    days_total += 1
    if days_spend == days_total == 5:
        break

if owned_money >= needed_money:
    print(f"You saved the money for {days_total} days.")
if days_spend == 5:
    print("You can\'t save the money.")
    print(days_spend)



