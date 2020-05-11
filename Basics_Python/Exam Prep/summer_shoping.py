budget = int(input())
towel = float(input())
discount = int(input())

umbrela = 2 /3 * towel
flips = 0.75 * umbrela
bag = 1/3 * (flips + towel)

price = towel + umbrela + flips + bag
price_discount = price - (price * discount/100)

if price_discount <= budget:
    print(f"Annie's sum is {price_discount:.2f} lv. She has {(budget - price_discount):.2f} lv. left.")
else:
    print(f"Annie's sum is {price_discount:.2f} lv. She needs {(abs(price_discount - budget)):.2f} lv. more.")