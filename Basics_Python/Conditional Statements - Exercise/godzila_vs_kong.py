budget = float(input())
actors_count = int(input())
costum_price = float(input())

costum_price_total = costum_price * actors_count
decor = budget * 0.1
razhodi = costum_price_total + decor

if actors_count >= 150:
    costum_price_total = costum_price_total * 0.9
    razhodi = costum_price_total + decor

if razhodi > budget:
    print('Not enough money!')
    print(f'Wingard needs {(razhodi - budget):.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {(budget - razhodi):.2f} leva left.')
