type_travel = input()
cabin_type = input()
nights = int(input())
price_per_night = 0

if type_travel == "Mediterranean":
    if cabin_type == "standard cabin":
        price_per_night = 27.50
    elif cabin_type == "cabin with balcony":
        price_per_night = 30.20
    elif cabin_type == "apartment":
        price_per_night = 40.50

elif type_travel == "Adriatic":
    if cabin_type == "standard cabin":
        price_per_night = 22.99
    elif cabin_type == "cabin with balcony":
        price_per_night = 25.00
    elif cabin_type == "apartment":
        price_per_night = 34.99

elif type_travel == "Aegean":
    if cabin_type == "standard cabin":
        price_per_night = 23.00
    elif cabin_type == "cabin with balcony":
        price_per_night = 26.60
    elif cabin_type == "apartment":
        price_per_night = 39.80

if nights > 7:
    price = 0.75 * (nights * price_per_night * 4)
else:
    price = nights * price_per_night * 4

print(f"Annie's holiday in the {type_travel} sea costs {price:.2f} lv.")