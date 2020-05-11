lillys_age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

money_given = 10
savings = 0
toys = 0
for year in range(1, lillys_age + 1):
    if year % 2 == 0:
        savings += money_given
        money_given += 10
        savings -= 1
    else:
        toys += 1

money_from_toys = toys * single_toy_price
savings += money_from_toys

if savings >= washing_machine_price:
    money_left = savings - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washing_machine_price - savings
    print(f"No! {money_needed:.2f}")