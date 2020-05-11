flowers = input()
count = int(input())
budget = int(input())

price_roses = 5
price_dahlias = 3.8
price_tulip = 2.8
price_narcissus = 3
price_gladiolus = 2.50

if "Roses" == flowers:
    if count > 80:
        price = count * price_roses * 0.9
    else:
        price = count * price_roses
elif "Dahlias" == flowers:
    if count > 90:
        price = count * price_dahlias * 0.85
    else:
        price = count * price_dahlias
elif "Tulips" == flowers:
    if count > 80:
        price = count * price_tulip * 0.85
    else:
        price = count * price_tulip
elif "Narcissus" == flowers:
    if count < 120:
        price = count * price_narcissus * 1.15
    else:
        price = count * price_narcissus
elif "Gladiolus" == flowers:
    if count < 80:
        price = count * price_gladiolus * 1.20
    else:
        price = count * price_gladiolus


if budget >= price:
    rest = budget - price
    print(f"Hey, you have a great garden with {count} {flowers} and {rest:.2f} leva left.")
else:
    rest = price - budget
    print(f"Not enough money, you need {rest:.2f} leva more.")