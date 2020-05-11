from math import ceil

sushi = input()
restorant_name = input()
portions_count = float(input())
delivery = input()

if restorant_name == "Sushi Zone" or restorant_name == "Sushi Time" or restorant_name == "Sushi Bar" or restorant_name == "Asian Pub":

    if  restorant_name == "Sushi Zone":
        if sushi == "sashimi":
            price = 4.99
        elif sushi == "maki":
            price = 5.29
        elif sushi == "uramaki":
            price = 5.99
        elif sushi == "temaki":
            price = 4.29

    elif  restorant_name == "Sushi Time":
        if sushi == "sashimi":
            price = 5.49
        elif sushi == "maki":
            price = 4.69
        elif sushi == "uramaki":
            price = 4.49
        elif sushi == "temaki":
            price = 5.19

    elif  restorant_name == "Sushi Bar":
        if sushi == "sashimi":
            price = 5.25
        elif sushi == "maki":
            price = 5.55
        elif sushi == "uramaki":
            price = 6.25
        elif sushi == "temaki":
            price = 4.75

    elif restorant_name == "Asian Pub":
        if sushi == "sashimi":
            price = 4.50
        elif sushi == "maki":
            price = 4.80
        elif sushi == "uramaki":
            price = 5.50
        elif sushi == "temaki":
            price = 5.50
    price_sushi = portions_count * price
    price_sushi_total = 0

    if delivery == "Y":
        price_sushi_total = 1.2 * price_sushi
        price_ceil = ceil(price_sushi_total)
        print(f"Total price: {price_ceil} lv.")
    else:
        print(f"Total price: {ceil(price_sushi)} lv.")

else:
    print(f"{restorant_name} is invalid restaurant!")


