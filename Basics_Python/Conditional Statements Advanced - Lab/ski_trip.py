days = int(input())
country = str(input())
ratting = input()

discount = 0
price = 0
nights = days - 1

if "France" == country:
    price
    if days < 10:
        discount = 0
        price = 18
    elif 10 <= days < 15:
        discount = 0
        price = 18
    elif 15 <= days:
        discount = 0
        price = 18
elif "Italy" == country:
    if days < 10:
        discount = 0.3
        price = 25
    elif 10 <= days < 15:
        discount = 0.35
        price = 25
    elif 15 <= days:
        discount = 0.5
        price = 25
elif "Germany" == country:
    if days < 10:
        discount = 0.10
        price = 35
    elif 10 <= days < 15:
        discount = 0.15
        price = 35
    elif 15 <= days:
        discount = 0.20
        price = 35

if 'positive' == ratting:
    discount_price = (nights * price) - (nights * price) * discount
    discount_after_ratting = discount_price * 1.25
    print(f"{discount_after_ratting:.2f}")
elif 'negative' == ratting:
    discount_price = (nights * price) - (nights * price) * discount
    discount_after_ratting = discount_price - discount_price * 0.10
    print(f"{discount_after_ratting:.2f}")
